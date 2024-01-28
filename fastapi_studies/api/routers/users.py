from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio.client import Redis

from fastapi_studies.api.dependencies import get_db_session, get_redis_client

users_router = APIRouter(prefix="/users")


@users_router.get("/all")
async def get_all_users(
        # db_session: AsyncSession = Depends(get_db_session),
        # redis: Redis = Depends(get_redis_client)
):
    # print(type(db_session))
    # print(redis, await redis.ping())
    return {"hello": "users"}


@users_router.get("/{user_id}")
async def get_user(
        user_id: int,
        # db_session: AsyncSession = Depends(get_db_session),
        # redis: Redis = Depends(get_redis_client)
):
    # print(type(db_session))
    # print(redis, await redis.ping())
    return {"hello": "user"}
