from fastapi_studies.api.routers.user.response import UserResponse
from fastapi_studies.api.routers.user.response import UsersResponse


async def test_user_endpoint(api_client):

    expected_response = UserResponse(
        name="Peter K.", age=33, hobby="programming"
    )

    response = await api_client.get("/users/get")
    assert response.status_code == 200
    assert response.json() == expected_response.model_dump()


async def test_users_endpoint(api_client):

    expected_response = UsersResponse(
        total=3,
        users=[UserResponse(name=f"User_{i}", age=i, hobby="abstract hobby")
               for i in [15, 35, 40]]
    )

    response = await api_client.get("/users/get_all")
    assert response.status_code == 200
    assert response.json() == expected_response.model_dump()
