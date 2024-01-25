from abc import abstractmethod
from typing import Protocol, Sequence, TypeVar

FilterParamsT = TypeVar("FilterParamsT")
MovieT = TypeVar("MovieT")


class MovieReader(Protocol[FilterParamsT, MovieT]):

    @abstractmethod
    async def get_movies_by_genre_and_year(
            self,
            params: FilterParamsT
    ) -> Sequence[MovieT]:
        raise NotImplementedError
