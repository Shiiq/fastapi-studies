from fastapi_studies.api.routers.request import MovieFindRequest
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.models import Movie, MovieFindData


class MovieFindService:

    def __init__(self, movie_repo: MovieReader):
        self._movie_repo = movie_repo

    async def __call__(
            self,
            request_data: MovieFindRequest
    ) -> ...:
        filter_data = self._get_filter_data(request_data)

        pass

    def _get_filter_data(
            self,
            request_data: MovieFindRequest
    ) -> MovieFindData:
        filter_data = MovieFindData()
        filter_data.genre = request_data.genre or None
        if request_data.year_from > request_data.year_to:
            filter_data.year_from = request_data.year_to
            filter_data.year_to = request_data.year_from
        return filter_data

    async def _get_movies(
            self,
            filter_data: MovieFindData
    ) -> list[Movie]:
        movies_orm = await self._movie_repo.get_movies_by_genre_and_year(filter_data)
        pass
