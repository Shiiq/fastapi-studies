import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from fastapi_studies.infrastructure.database.config import DBConfig
from fastapi_studies.infrastructure.database.connection import create_engine


@pytest.fixture(scope="session")
def db_config():
    test_db_config = DBConfig(db_url="./fastapi_studies_test.db")
    return test_db_config


@pytest_asyncio.fixture(scope="session")
async def db_connection(db_config):
    engine = create_engine(db_config)
    async with engine.connect() as conn:
        yield conn
    await engine.dispose()
