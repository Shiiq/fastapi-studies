from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio.client import Redis

from fastapi_studies.api.dependencies import get_db_session, get_redis_client

movies_router = APIRouter(prefix="/movies")


# @movies_router.get()
async def get_movies():

    pass
