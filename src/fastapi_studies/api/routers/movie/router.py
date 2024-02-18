from fastapi import APIRouter, Depends, Request, status

from fastapi_studies.api.dependencies.stub import Stub
from fastapi_studies.api.routers.movie.paginator import MoviePaginator
from fastapi_studies.api.routers.movie.request import MovieRequest
from fastapi_studies.api.routers.movie.request import PaginationRequest
from fastapi_studies.api.routers.movie.response import MovieResponse
from fastapi_studies.api.routers.movie.response import MoviePaginatedResponse
from fastapi_studies.application.movie.constants import GENRE_DEFAULT
from fastapi_studies.application.movie.constants import YEAR_FROM_DEFAULT
from fastapi_studies.application.movie.constants import YEAR_TO_DEFAULT
from fastapi_studies.application.movie.models import MovieFilterParams
from fastapi_studies.application.movie.services import MovieFindService

movie_router = APIRouter(prefix="/movies")


def get_movie_filter_params(request_data: MovieRequest) -> MovieFilterParams:
    request_data.genre.sort()
    genre = request_data.genre or GENRE_DEFAULT
    year_from = request_data.year_from or YEAR_FROM_DEFAULT
    year_to = request_data.year_to or YEAR_TO_DEFAULT
    if year_from > year_to:
        year_from, year_to = year_to, year_from
    return MovieFilterParams(
        genre=genre, year_from=year_from, year_to=year_to
    )


@movie_router.get(
    path="/get",
    response_model=MoviePaginatedResponse,
    status_code=status.HTTP_200_OK,
    tags=["movies", ]
)
async def get_movies_by_genre(
        request: Request,
        request_data: MovieRequest = Depends(),
        movie_finder: Stub(MovieFindService) = Depends(),
        pagination_data: PaginationRequest = Depends(),
        paginator: MoviePaginator = Depends(),
) -> MoviePaginatedResponse:

    filter_params = get_movie_filter_params(request_data)
    pagination_params = paginator.get_params(pagination_data)
    movies = await movie_finder(
        filter_params=filter_params, pagination_params=pagination_params
    )
    return paginator.create_response(
        base_url=request.url, movies_data=movies
    )


@movie_router.get(
    path="/get/{movie_id}",
    response_model=MovieResponse,
    tags=["movies", ]
)
async def get_movie_by_id(
        movie_id: int,
        movie_finder: Stub(MovieFindService) = Depends()
) -> MovieResponse:

    movie = await movie_finder.get_by_id(movie_id)
    return MovieResponse(
        id=movie_id, title=movie.title, year=movie.year, genres=movie.genres
    )
