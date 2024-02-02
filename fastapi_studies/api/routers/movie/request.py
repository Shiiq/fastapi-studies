from fastapi import Query
from pydantic import BaseModel, Field, PositiveInt


class MovieRequest(BaseModel):

    genre: list[str] = Field(Query([]))
    year_from: PositiveInt | None = Field(Query(None))
    year_to: PositiveInt | None = Field(Query(None))


class PaginationRequest(BaseModel):

    page: int = Field(Query(1))
