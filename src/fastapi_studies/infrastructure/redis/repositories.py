from dataclasses import asdict
from typing import Iterator, Sequence

import orjson
from redis.asyncio.client import Redis

from fastapi_studies.application.movie.common import CacheStorageKey
from fastapi_studies.application.movie.common import MovieJSON
from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.models import Movie as MovieDTO
from fastapi_studies.application.movie.models import MoviePaginationParams


def movie_dto_to_json(input_data: MovieDTO) -> MovieJSON:
    movie_as_dict = asdict(input_data)
    return MovieJSON(orjson.dumps(movie_as_dict))


def movie_json_to_dto(input_data: MovieJSON) -> MovieDTO:
    movie_as_dict = orjson.loads(input_data)
    return MovieDTO(
        title=movie_as_dict["title"],
        year=int(movie_as_dict["year"]),
        genres=movie_as_dict["genres"]
    )


class MovieCacheRepo(MovieCache):

    def __init__(self, redis_client: Redis):
        self._redis = redis_client

    async def get_items_count(
            self,
            key: CacheStorageKey
    ) -> int:
        return await self._redis.llen(key)

    async def read(
            self,
            key: CacheStorageKey,
            pagination_params: MoviePaginationParams
    ) -> Iterator[MovieDTO]:
        movies = await self._redis.lrange(
            name=key,
            start=pagination_params.start,
            end=pagination_params.end - 1
        )
        return map(movie_json_to_dto, movies)

    async def write(
            self,
            key: CacheStorageKey,
            movies: Sequence[MovieDTO]
    ) -> int:
        movies = map(movie_dto_to_json, movies)
        return await self._redis.rpush(key, *movies)
