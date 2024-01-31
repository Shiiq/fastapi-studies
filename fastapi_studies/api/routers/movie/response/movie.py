from pydantic import BaseModel

from fastapi_studies.application.movie.models import Movie


class MoviePaginatedResponse(BaseModel):

    page: int
    movies: list[Movie] = []
    total_movies_count: int
    next_page: str | None = None
    prev_page: str | None = None
