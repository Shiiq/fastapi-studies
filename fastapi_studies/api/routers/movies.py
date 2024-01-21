from fastapi import APIRouter, Depends, Query

from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio.client import Redis

from fastapi_studies.api.dependencies import get_db_session, get_redis_client
from fastapi_studies.api.dependencies.setup import DBG


movies_router = APIRouter(prefix="/movies")


@movies_router.get("/get")
async def get_movies_by_genre(
        genre: list[str] = Query(default=None),
        dbgw: DBG = Depends()
):
    print(genre, type(genre))
    print(f"DB GATEWAY ID {id(dbgw)}, SESSION ID {id(dbgw.s)}")
    return {"hello": "world"}
