from abc import abstractmethod
from typing import Iterator, Protocol, Sequence

from fastapi_studies.application.movie.common import CacheStorageKey
from fastapi_studies.application.movie.models import Movie
from fastapi_studies.application.movie.models import MovieFilterParams
from fastapi_studies.application.movie.models import MoviePaginationParams


class MovieCache(Protocol):

    @abstractmethod
    async def get_items_count(
            self,
            key: CacheStorageKey
    ) -> int:
        raise NotImplementedError

    @abstractmethod
    async def read(
            self,
            key: CacheStorageKey,
            pagination_params: MoviePaginationParams
    ) -> Iterator[Movie]:
        raise NotImplementedError

    @abstractmethod
    async def write(
            self,
            key: CacheStorageKey,
            movies: Sequence[Movie]
    ) -> int:
        raise NotImplementedError


class MovieReader(Protocol):

    @abstractmethod
    async def get_by_genre_and_year(
            self,
            filter_params: MovieFilterParams
    ) -> Iterator[Movie]:
        raise NotImplementedError
