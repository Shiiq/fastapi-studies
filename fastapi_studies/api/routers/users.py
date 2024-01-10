from fastapi import APIRouter, Depends

from fastapi_studies.api.dependencies import get_redis_client

users_router = APIRouter(prefix="/users")


@users_router.get("/{user_id}")
async def get_user(user_id: str, redis=Depends(get_redis_client)):
    print(redis, await redis.ping())
    return {"hello": "user"}


@users_router.get("/all")
async def get_all_users(redis=Depends(get_redis_client)):
    print(redis, await redis.ping())
    return {"hello": "users"}
