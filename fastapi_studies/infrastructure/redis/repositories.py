from typing import Iterable, Sequence

from redis.asyncio.client import Redis

from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.models import Movie, MoviePagination


class MovieCacheRepo(MovieCache):

    def __init__(self, redis_client: Redis):
        self._redis = redis_client

    async def check_existence(
            self,
            key: str
    ) -> bool:
        exist = await self._redis.llen(key)
        return bool(exist)

    async def read(
            self,
            key: str,
            pagination_params: MoviePagination | None = None
    ):
        if pagination_params:
            movies = await self._redis.lrange(
                key, pagination_params.start, pagination_params.end - 1
            )
            return movies
        movies = await self._redis.lrange(key, 0, -1)
        return movies

    async def write(self, key: str, *movies):
        await self._redis.rpush(key, *movies)
