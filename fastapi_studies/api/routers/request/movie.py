from fastapi import Query
from pydantic import BaseModel, Field, PositiveInt


class MovieFindRequest(BaseModel):

    genre: list[str] | None = Field(Query(None))
    year_from: PositiveInt | None = Field(Query(1))
    year_to: PositiveInt | None = Field(Query(9999))
