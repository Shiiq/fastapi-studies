from contextlib import asynccontextmanager
from typing import AsyncIterator

from redis.asyncio.client import Redis

from .config import RedisConfig


@asynccontextmanager
async def get_redis_client(
        redis_config: RedisConfig
) -> AsyncIterator[Redis]:

    redis_client = Redis(host=redis_config.host, port=redis_config.port)
    yield redis_client
    await redis_client.aclose()
