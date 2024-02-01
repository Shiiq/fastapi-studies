from typing import Iterable, Sequence

from fastapi_studies.application.movie.exceptions import MoviesNotFound
from fastapi_studies.application.movie.exceptions import MoviesOutOfRange
from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.models import Movie
from fastapi_studies.application.movie.models import MoviesList
from fastapi_studies.application.movie.models import MovieFilterData
from fastapi_studies.application.movie.models import MoviePagination
from fastapi_studies.api.routers.movie.request import MovieFilterRequest
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
            pagination_params: MoviePagination,
    ) -> MoviesList:
        x = MoviePagination(0, 15, 1)
        filter_params = self._get_filter_params(request_data)
        self._set_cache_uid(filter_params)
        movies_list = await self._get_movies(filter_params, x)
        return movies_list

    def _get_filter_params(
            self,
            request_data: MovieFilterRequest
    ) -> MovieFilterData:
        request_data.genre.sort()
        genre = request_data.genre or GENRE_DEFAULT
        year_from = request_data.year_from or YEAR_FROM_DEFAULT
        year_to = request_data.year_to or YEAR_TO_DEFAULT
        if year_from > year_to:
            year_from, year_to = year_to, year_from
        return MovieFilterData(
            genre=genre, year_from=year_from, year_to=year_to
        )

    def _set_cache_uid(
            self,
            filter_params: MovieFilterData
    ):
        cache_uid = (
            "movies:"
            f"{('-').join(filter_params.genre) if filter_params.genre else 'all'}:"
            f"{filter_params.year_from}-{filter_params.year_to}"
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
    ) -> int:
        movies_as_json = map(movie_dto_to_json, movies)
        movies_count = await self._movie_cache.write(key, *movies_as_json)
        return movies_count

    def _validate_pagination_params(
            self,
            items_count: int,
            pagination_params: MoviePagination
    ) -> bool:
        return pagination_params.start < items_count

    async def _get_movies(
            self,
            filter_params: MovieFilterData,
            pagination_params: MoviePagination | None = None
    ) -> MoviesList:

        movies_count = await self._movie_cache.get_items_count(
            filter_params.cache_uid
        )

        # means that the cache is emtpy
        if movies_count == 0:
            movies = list(await self._get_from_db(filter_params))

            # means that we don't have movies with these parameters
            if not movies:
                raise MoviesNotFound
                # return MoviesList(
                #     movies=[],
                #     total_count=movies_count,
                #     current_page=pagination_params.page
                # )

            # upload movies to the cache - return value is the number of movies
            movies_uploaded = await self._write_to_cache(
                key=filter_params.cache_uid, movies=movies
            )

            # check that current pagination params match with number of movies
            if not self._validate_pagination_params(
                    items_count=movies_uploaded,
                    pagination_params=pagination_params
            ):
                raise MoviesOutOfRange
                # return MoviesList(
                #     movies=[],
                #     total_count=movies_count,
                #     current_page=pagination_params.page
                # )

            return MoviesList(
                movies=movies[pagination_params.start:pagination_params.end],
                total_count=movies_count,
                current_page=pagination_params.page
            )

        # this means that the cache is not emtpy
        else:
            if not self._validate_pagination_params(
                    items_count=movies_count,
                    pagination_params=pagination_params
            ):
                raise MoviesOutOfRange
            movies = list(await self._read_from_cache(
                key=filter_params.cache_uid,
                pagination_params=pagination_params
            ))
            return MoviesList(
                movies=movies,
                total_count=movies_count,
                current_page=pagination_params.page
            )
