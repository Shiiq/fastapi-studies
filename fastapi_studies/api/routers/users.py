from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio.client import Redis

from fastapi_studies.api.dependencies import get_db_session, get_redis_client
from fastapi_studies.api.dependencies.stub import Stub

users_router = APIRouter(prefix="/users")


@users_router.get("/{user_id}")
async def get_user(
        user_id: str,
        # db_session=Depends(Stub(get_db_session)),
        db_session=Depends(Stub(AsyncSession)),
        redis: Redis = Depends(get_redis_client)
):
    print(type(db_session))
    # print(type(await db_session.asend(None)))
    print(redis, await redis.ping())
    return {"hello": "user"}


@users_router.get("/all")
async def get_all_users(
        # db_session=Depends(Stub(get_db_session)),
        db_session=Depends(Stub(AsyncSession)),
        redis: Redis = Depends(get_redis_client)
):
    print(type(db_session))
    # print(type(await db_session.asend(None)))
    print(redis, await redis.ping())
    return {"hello": "users"}
