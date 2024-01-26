from fastapi import APIRouter, Depends

from fastapi_studies.api.routers.request import MovieFindRequest
from fastapi_studies.infrastructure.database.repositories import MovieRepo
from fastapi_studies.api.dependencies.stub import Stub

movies_router = APIRouter(prefix="/movies")


@movies_router.get("/get")
async def get_movies_by_genre(
        movie_filter_params: MovieFindRequest = Depends(),
        movie_repo: Stub(MovieRepo) = Depends()
):
    print("QUERY PARAMS", movie_filter_params)
    movies = await movie_repo.get_movies_by_genre_and_year(movie_filter_params)
    print(len(movies))
    for m in movies:
        print(m.title)
    # print(genre, type(genre))
    # print(
    #     f"DB GATEWAY ID {id(movie_repo)}, "
    #     f"SESSION ID {id(movie_repo._session)}"
    # )
    return {"hello": "world"}
