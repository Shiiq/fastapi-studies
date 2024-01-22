from fastapi import APIRouter, Depends, Query

from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio.client import Redis

from fastapi_studies.api.dependencies import get_db_session, get_redis_client
from fastapi_studies.infrastructure.database.repositories import MovieRepo
from fastapi_studies.api.dependencies.stub import Stub

movies_router = APIRouter(prefix="/movies")


@movies_router.get("/get")
async def get_movies_by_genre(
        genre: list[str] = Query(default=None),
        movie_repo: Stub(MovieRepo) = Depends()
):
    print(genre, type(genre))
    print(
        f"DB GATEWAY ID {id(movie_repo)}, "
        f"SESSION ID {id(movie_repo._session)}"
    )
    return {"hello": "world"}
