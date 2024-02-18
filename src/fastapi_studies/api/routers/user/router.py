from fastapi import APIRouter, status

from fastapi_studies.api.routers.user.response import UserResponse
from fastapi_studies.api.routers.user.response import UsersResponse

user_router = APIRouter(prefix="/users")


@user_router.get(
    path="/get",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["users", ]
)
async def get_user() -> UserResponse:
    return UserResponse(
        name="Peter K.", age=33, hobby="programming"
    )


@user_router.get(
    path="/get_all",
    response_model=UsersResponse,
    status_code=status.HTTP_200_OK,
    tags=["users", ]
)
async def get_users() -> UsersResponse:
    return UsersResponse(
        total=3,
        users=[UserResponse(name=f"User_{i}", age=i, hobby="abstract hobby")
               for i in [15, 35, 40]]
    )
