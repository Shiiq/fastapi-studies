from typing import Iterable, Sequence

from redis.asyncio.client import Redis

from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.models import MoviePagination


class MovieCacheRepo(MovieCache):

    def __init__(self, redis_client: Redis):
        self._redis = redis_client

    async def get_items_count(
            self,
            key: str
    ) -> int:
        count = await self._redis.llen(key)
        return count

    async def read(
            self,
            key: str,
            pagination_params: MoviePagination | None = None
    ):
        if pagination_params:
            movies = await self._redis.lrange(
                name=key,
                start=pagination_params.start,
                end=pagination_params.end - 1
            )
            return movies
        movies = await self._redis.lrange(name=key, start=0, end=-1)
        return movies

    async def write(self, key: str, *movies) -> int:
        movies_count = await self._redis.rpush(key, *movies)
        return movies_count
