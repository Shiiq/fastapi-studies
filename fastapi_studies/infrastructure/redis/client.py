import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import redis.asyncio as redis
from redis.asyncio.client import Redis

from .config import RedisConfig


@asynccontextmanager
async def get_redis_client(
        redis_config: RedisConfig
) -> AsyncGenerator[Redis, None]:
    redis_client = redis.Redis(
        host=redis_config.host,
        port=redis_config.port
    )
    print("yielding redis client")
    yield redis_client
    print("closing redis client")
    await redis_client.aclose()


# async def check():
#     client = redis.Redis()
#     print(type(client))
#     print(f"Ping successful: {await client.ping()}")
#     await client.aclose()
#
#
# asyncio.run(check())
