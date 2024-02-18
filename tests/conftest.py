import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient

from fastapi_studies.api.routers.movie.response import MovieResponse
from fastapi_studies.infrastructure.database.config import DBConfig
from fastapi_studies.infrastructure.database.connection import create_engine


@pytest.fixture
def app():
    from fastapi_studies.main import app
    yield app


@pytest.fixture
async def api_client(app):
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client
