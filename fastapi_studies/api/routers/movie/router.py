from fastapi import APIRouter, Depends, Request

from fastapi_studies.api.dependencies.stub import Stub
from fastapi_studies.api.routers.movie.request import MovieFilterRequest
from fastapi_studies.api.routers.movie.request import PaginationRequest
from fastapi_studies.application.movie.services import MovieFindService

movie_router = APIRouter(prefix="/movies")


@movie_router.get("/get")
async def get_movies_by_genre(
        request: Request,
        movie_filter_params: MovieFilterRequest = Depends(),
        movie_find: Stub(MovieFindService) = Depends(),
        pagination: PaginationRequest = Depends(),
):
    print("QUERY PARAMS", movie_filter_params)
    print("PAGINATION", pagination)
    res = await movie_find(movie_filter_params, pagination)
    print(res)
    return {"hello": "world"}
