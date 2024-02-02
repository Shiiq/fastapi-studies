from contextlib import asynccontextmanager
from typing import AsyncContextManager

import redis.asyncio as redis
from redis.asyncio.client import Redis

from .config import RedisConfig


@asynccontextmanager
async def get_redis_client(
        redis_config: RedisConfig
) -> AsyncContextManager[Redis]:

    redis_client = redis.Redis(
        host=redis_config.host,
        port=redis_config.port
    )
    yield redis_client
    await redis_client.aclose()
