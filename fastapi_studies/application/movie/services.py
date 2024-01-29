from fastapi_studies.api.routers.request import MovieFilterRequest
from fastapi_studies.api.routers.request import PaginationRequest
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.models import Movie
from fastapi_studies.application.movie.models import MoviesList
from fastapi_studies.application.movie.models import MovieFilterData
from fastapi_studies.application.movie.models import MoviePagination
from .constants import GENRE_DEFAULT, YEAR_FROM_DEFAULT, YEAR_TO_DEFAULT


class MovieFindService:

    def __init__(self, movie_reader: MovieReader):
        self._movie_reader = movie_reader

    async def __call__(
            self,
            request_data: MovieFilterRequest,
            pagination_data: PaginationRequest
    ) -> MoviesList:


        filter_params = self._get_filter_params(request_data)
        pagination_params = self._get_pagination_params(pagination_data)
        movies = await self._get_movies(filter_params)
        return MoviesList(movies=movies, total_count=len(movies))

    def _get_filter_params(
            self,
            request_data: MovieFilterRequest
    ) -> MovieFilterData:

        genre = request_data.genre or GENRE_DEFAULT
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

        offset = (pagination_data.page - 1) * pagination_data.per_page
        return MoviePagination(
            limit=pagination_data.per_page,
            offset=offset
        )

    async def _get_movies(
            self,
            filter_params: MovieFilterData,
            pagination_params: MoviePagination | None = None
    ) -> list[Movie]:

        movies = await self._movie_reader.get_by_genre_and_year(
            filter_params=filter_params,
            pagination_params=pagination_params
        )
        movies = [
            Movie(genres=movie.genre, title=movie.title, year=movie.year)
            for movie in movies
        ]
        return movies
