from fastapi import Query
from pydantic import BaseModel, Field, PositiveInt


class MovieFilterRequest(BaseModel):

    genre: list[str] | None = Field(Query(None))
    year_from: PositiveInt | None = Field(Query(None))
    year_to: PositiveInt | None = Field(Query(None))
