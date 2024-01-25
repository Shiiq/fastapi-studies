from pydantic import BaseModel


class Pagination(BaseModel):

    page: int = 1
    limit: int = 15

    # next_page: str = ""
    # prev_page: str = ""
