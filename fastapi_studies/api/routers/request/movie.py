from fastapi import Query
from pydantic import BaseModel, NonNegativeInt, PositiveInt


class MovieFilterParams(BaseModel):

    genre: list[str] = Query(default=[""])
    year_from: NonNegativeInt = Query(default=0)
    year_to: PositiveInt = Query(default=9999)
