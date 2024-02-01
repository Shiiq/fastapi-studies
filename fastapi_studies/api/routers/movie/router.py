from fastapi import APIRouter, Depends, Request

from fastapi_studies.api.dependencies.stub import Stub
from fastapi_studies.api.routers.common.paginator import Paginator
from fastapi_studies.api.routers.movie.request import MovieRequest
from fastapi_studies.api.routers.movie.request import PaginationRequest
from fastapi_studies.api.routers.movie.response import MoviePaginatedResponse
from fastapi_studies.application.movie.constants import GENRE_DEFAULT
from fastapi_studies.application.movie.constants import YEAR_FROM_DEFAULT
from fastapi_studies.application.movie.constants import YEAR_TO_DEFAULT
from fastapi_studies.application.movie.models import MovieFilterParams
from fastapi_studies.application.movie.services import MovieFindService

movie_router = APIRouter(prefix="/movies")


def get_movie_filter_params(
        request_data: MovieRequest = Depends()
) -> MovieFilterParams:
    request_data.genre.sort()
    genre = request_data.genre or GENRE_DEFAULT
    year_from = request_data.year_from or YEAR_FROM_DEFAULT
    year_to = request_data.year_to or YEAR_TO_DEFAULT
    if year_from > year_to:
        year_from, year_to = year_to, year_from
    return MovieFilterParams(
        genre=genre, year_from=year_from, year_to=year_to
    )


@movie_router.get("/get")
async def get_movies_by_genre(
        request: Request,
        filter_params: MovieFilterParams = Depends(),
        movie_finder: Stub(MovieFindService) = Depends(),
        pagination_data: PaginationRequest = Depends(),
        paginator: Paginator = Depends(),
) -> MoviePaginatedResponse:

    pagination_params = paginator.get_params(pagination_data)
    movies = await movie_finder(
        filter_params=filter_params, pagination_params=pagination_params
    )
    response = paginator.create_response(
        base_url=request.url, movies_data=movies
    )
    return response
