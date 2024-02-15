from pydantic import BaseModel, Field


class UserResponse(BaseModel):

    name: str
    age: int = Field(gt=0)
    hobby: str


class UsersResponse(BaseModel):

    total: int
    users: list[UserResponse]
