from pydantic import BaseModel


class Pagination(BaseModel):

    page: int
    per_page: int
    # next_page: str = ""
    # prev_page: str = ""
