from dataclasses import dataclass

from fastapi_studies.application.movie.common import CacheStorageKey


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
class MovieFilterParams:

    genre: list[str] | None
    year_from: int
    year_to: int
    cache_key: CacheStorageKey | None = None


@dataclass
class MoviePaginationParams:

    start: int
    end: int
    page: int
