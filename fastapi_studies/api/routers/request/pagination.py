from fastapi import Query
from pydantic import BaseModel, Field


class PaginationRequest(BaseModel):

    page: int = Field(Query(1))
    per_page: int = Field(Query(5))
