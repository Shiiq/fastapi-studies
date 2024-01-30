from typing import Iterable, Sequence

from fastapi_studies.api.routers.request import MovieFilterRequest
from fastapi_studies.api.routers.request import PaginationRequest
from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.models import Movie
from fastapi_studies.application.movie.models import MoviesList
from fastapi_studies.application.movie.models import MovieFilterData
from fastapi_studies.application.movie.models import MoviePagination
from fastapi_studies.infrastructure.converters import movie_dto_to_json
from fastapi_studies.infrastructure.converters import movie_json_to_dto
from fastapi_studies.infrastructure.converters import movie_orm_to_dto

from .constants import GENRE_DEFAULT, YEAR_FROM_DEFAULT, YEAR_TO_DEFAULT


class MovieFindService:

    def __init__(self, movie_cache: MovieCache, movie_reader: MovieReader):
        self._movie_cache = movie_cache
        self._movie_reader = movie_reader

    async def __call__(
            self,
            request_data: MovieFilterRequest,
            pagination_data: PaginationRequest
    ) -> MoviesList:

        filter_params = self._get_filter_params(request_data)
        self._set_cache_uid(filter_params)
        pagination_params = self._get_pagination_params(pagination_data)
        movies_list = await self._get_movies(filter_params, pagination_params)
        return movies_list

    def _get_filter_params(
            self,
            request_data: MovieFilterRequest
    ) -> MovieFilterData:
        genre = request_data.genre.sort() or GENRE_DEFAULT
        year_from = request_data.year_from or YEAR_FROM_DEFAULT
        year_to = request_data.year_to or YEAR_TO_DEFAULT
        if year_from > year_to:
            year_from, year_to = year_to, year_from
        return MovieFilterData(
            genre=genre,
            year_from=year_from,
            year_to=year_to
        )

    def _get_pagination_params(
            self,
            pagination_data: PaginationRequest
    ) -> MoviePagination:
        start = (pagination_data.page - 1) * pagination_data.per_page
        return MoviePagination(
            start=start,
            end=start + pagination_data.per_page
        )

    def _set_cache_uid(
            self,
            filter_params: MovieFilterData
    ):
        cache_uid = (
            "movies:"
            f"{('-').join(filter_params.genre) if filter_params.genre else 'all'}:"
            f"{str(filter_params.year_from)}-{str(filter_params.year_to)}"
        )
        filter_params.cache_uid = cache_uid

    async def _get_from_db(
            self,
            filter_params: MovieFilterData,
            pagination_params: MoviePagination | None = None
    ) -> Iterable[Movie]:
        movies = await self._movie_reader.get_by_genre_and_year(
            filter_params=filter_params,
            pagination_params=pagination_params
        )
        return map(movie_orm_to_dto, movies)

    async def _read_from_cache(
            self,
            key: str,
            pagination_params: MoviePagination | None = None
    ) -> Iterable[Movie]:
        movies_as_str = await self._movie_cache.read(key, pagination_params)
        return map(movie_json_to_dto, movies_as_str)

    async def _write_to_cache(
            self,
            key: str,
            movies: Sequence[Movie]
    ):
        movies_as_json = map(movie_dto_to_json, movies)
        await self._movie_cache.write(key, *movies_as_json)

    async def _get_movies(
            self,
            filter_params: MovieFilterData,
            pagination_params: MoviePagination | None = None
    ):
        movies = list(await self._read_from_cache(
            key=filter_params.cache_uid,
            pagination_params=pagination_params
        ))
        if not movies:
            movies = list(await self._get_from_db(filter_params))
            await self._write_to_cache(
                key=filter_params.cache_uid,
                movies=movies
            )
        return MoviesList(
            movies=movies[pagination_params.start:pagination_params.end],
            total_count=len(movies)
        )
