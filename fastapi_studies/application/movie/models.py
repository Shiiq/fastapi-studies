from dataclasses import dataclass


@dataclass
class Movie:

    title: str
    year: int
    genres: list[str]


@dataclass
class MovieFilterData:

    genre: list[str]
    year_from: int
    year_to: int


@dataclass
class MoviePagination:

    limit: int = 15
    offset: int = 0
