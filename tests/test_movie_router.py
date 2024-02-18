from fastapi_studies.api.routers.movie.response import MovieResponse

from .mocks import FakeDB


async def test_movie_by_id_endpoint(api_client):

    api_client.dependency_override[] = ...

    expected_response = MovieResponse(
        id=125,
        title="Rob Roy",
        year=1995,
        genres=["romance", "drama", "action", "war"]
    )

    response = await api_client.get("/movies/get/125")
    assert response.status_code == 200
    assert response.json() == expected_response.model_dump()
