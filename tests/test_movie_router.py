import pytest
import pytest_asyncio

from fastapi_studies.api.routers.movie.response import MovieResponse

movie_response = MovieResponse(
    id=125,
    title="Rob Roy",
    year=1995,
    genres=["romance", "drama", "action", "war"]
)


# @pytest.mark.asyncio
async def test_movie_by_id_endpoint(api_client):
    response = await api_client.get("/movies/get/125")
    assert response.status_code == 200
    assert response.json() == movie_response.model_dump()
