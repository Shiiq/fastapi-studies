from pydantic import BaseModel

from fastapi_studies.application.movie.models import Movie


class MovieResponse(BaseModel):

    id: int
    title: str
    year: int
    genres: list[str]


class MoviePaginatedResponse(BaseModel):

    current_page: int
    next_page: str | None = None
    prev_page: str | None = None
    total_movies: int
    movies: list[Movie] = []
