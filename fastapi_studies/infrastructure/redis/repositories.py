from dataclasses import asdict
from json import dumps, loads
from typing import Iterator, Sequence

from redis.asyncio.client import Redis

from fastapi_studies.application.movie.common import CacheStorageKey, MovieJSON
from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.models import Movie as MovieDTO
from fastapi_studies.application.movie.models import MoviePaginationParams


def movie_dto_to_json(input_data: MovieDTO) -> MovieJSON:
    movie_as_dict = asdict(input_data)
    return dumps(movie_as_dict)


def movie_json_to_dto(input_data: MovieJSON) -> MovieDTO:
    movie_as_dict = loads(input_data)
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
        count = await self._redis.llen(key)
        return count

    async def read(
            self,
            key: CacheStorageKey,
            pagination_params: MoviePaginationParams | None = None
    ) -> Iterator[MovieDTO]:
        if pagination_params:
            movies = await self._redis.lrange(
                name=key,
                start=pagination_params.start,
                end=pagination_params.end - 1
            )
            return map(movie_json_to_dto, movies)
        movies = await self._redis.lrange(name=key, start=0, end=-1)
        return map(movie_json_to_dto, movies)

    async def write(
            self,
            key: CacheStorageKey,
            movies: Sequence[MovieDTO]
    ) -> int:
        movies = map(movie_dto_to_json, movies)
        movies_count = await self._redis.rpush(key, *movies)
        return movies_count
