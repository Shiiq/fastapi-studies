import pytest
import pytest_asyncio
from httpx import AsyncClient

from fastapi_studies.infrastructure.database.config import DBConfig
from fastapi_studies.infrastructure.database.connection import create_engine


# @pytest.fixture(scope="session")
# def db_config():
#     test_db_config = DBConfig(db_url="./fastapi_studies_test.db")
#     return test_db_config


# @pytest.fixture(scope="session")
# async def db_connection(db_config):
#     engine = create_engine(db_config)
#     async with engine.connect() as conn:
#         yield conn
#     await engine.dispose()

@pytest.fixture()
def app():
    from fastapi_studies.main import app
    yield app


@pytest.fixture()
async def api_client(app):
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client


# @pytest.fixture
# def anyio_backend():
#     return "asyncio"
