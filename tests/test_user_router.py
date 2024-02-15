from fastapi.testclient import TestClient

from fastapi_studies.main import app
from fastapi_studies.api.routers.user.response import UserResponse
from fastapi_studies.api.routers.user.response import UsersResponse


client = TestClient(app)
user_response = UserResponse(name="Peter K.", age=33, hobby="programming")
users_response = UsersResponse(
    total=3,
    users=[UserResponse(name=f"User_{i}", age=i, hobby="abstract hobby")
           for i in [15, 35, 40]])


def test_user_endpoint():
    response = client.get("/users/get")
    assert response.status_code == 200
    assert response.json() == user_response.model_dump()


def test_users_endpoint():
    response = client.get("/users/get_all")
    assert response.status_code == 200
    assert response.json() == users_response.model_dump()
