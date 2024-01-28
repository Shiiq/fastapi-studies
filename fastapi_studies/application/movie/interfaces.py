from abc import abstractmethod
from typing import Protocol, Sequence, TypeVar

MovieT = TypeVar("MovieT")
MovieFilterParamsT = TypeVar("MovieFilterParamsT")
MoviePaginationParamsT = TypeVar("MoviePaginationParamsT")


class MovieReader(Protocol[MovieT, MovieFilterParamsT]):

    @abstractmethod
    async def get_by_genre_and_year(
            self,
            filter_params: MovieFilterParamsT,
            pagination_params: MoviePaginationParamsT | None,
    ) -> Sequence[MovieT]:
        raise NotImplementedError
