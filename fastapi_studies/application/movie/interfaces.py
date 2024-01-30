from abc import abstractmethod
from typing import Protocol, Sequence, TypeVar

CollectionKeyT = TypeVar("CollectionKeyT")
MovieT = TypeVar("MovieT")
MovieFilterParamsT = TypeVar("MovieFilterParamsT")
MoviePaginationParamsT = TypeVar("MoviePaginationParamsT")


class MovieCache(Protocol[CollectionKeyT, MovieT]):

    @abstractmethod
    async def check_existence(
            self,
            key: CollectionKeyT
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def read(
            self,
            key: CollectionKeyT
    ) -> Sequence[MovieT]:
        raise NotImplementedError

    @abstractmethod
    async def write(
            self,
            key: CollectionKeyT,
            *movies: MovieT
    ):
        raise NotImplementedError


class MovieReader(Protocol[MovieT, MovieFilterParamsT]):

    @abstractmethod
    async def get_by_genre_and_year(
            self,
            filter_params: MovieFilterParamsT,
            pagination_params: MoviePaginationParamsT | None,
    ) -> Sequence[MovieT]:
        raise NotImplementedError
