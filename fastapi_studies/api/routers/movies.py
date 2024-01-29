from fastapi import APIRouter, Depends, Request

from fastapi_studies.api.dependencies.stub import Stub
from fastapi_studies.api.routers.request import MovieFilterRequest
from fastapi_studies.api.routers.request import PaginationRequest
from fastapi_studies.application.movie.services import MovieFindService

movies_router = APIRouter(prefix="/movies")


@movies_router.get("/get")
async def get_movies_by_genre(
        movie_filter_params: MovieFilterRequest = Depends(),
        movie_find: Stub(MovieFindService) = Depends(),
        pagination: PaginationRequest = Depends(),
        request: Request = Depends()
):
    print("QUERY PARAMS", movie_filter_params)
    print("PAGINATION", pagination)
    res = await movie_find(movie_filter_params)
    print(res)
    return {"hello": "world"}
