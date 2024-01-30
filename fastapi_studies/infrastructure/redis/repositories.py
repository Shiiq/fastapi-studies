from typing import Iterable, Sequence

from redis.asyncio.client import Redis

from fastapi_studies.application.movie.interfaces import MovieCache


class MovieCacheRepo(MovieCache):

    def __init__(self, redis_client: Redis):
        self._redis = redis_client

    async def check_existence(self, key: str) -> bool:
        exist = await self._redis.llen(key)
        return bool(exist)

    async def read(self, key: str):

        pass

    async def write(self, key: str, *movies):
        await self._redis.rpush(key, *movies)
