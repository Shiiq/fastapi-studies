from dataclasses import dataclass


@dataclass
class Movie:

    title: str
    year: int
    genres: list[str]


@dataclass
class MoviesList:

    movies: list[Movie]
    current_page: int
    total_count: int


@dataclass
class MovieFilterData:

    genre: list[str] | None
    year_from: int
    year_to: int
    cache_uid: str | None = None


@dataclass
class MoviePagination:

    start: int
    end: int
    page: int
