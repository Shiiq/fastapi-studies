from functools import partial
from typing import AsyncGenerator

from fastapi import FastAPI, Depends
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_studies.infrastructure.database.repositories import MovieRepo
from fastapi_studies.api.dependencies.stub import Stub

def get_redis_client() -> Redis:
    raise NotImplementedError


def get_db_session() -> AsyncSession:
    raise NotImplementedError


def get_movie_repo(
        session: AsyncSession = Depends(get_db_session)
) -> MovieRepo:
    yield MovieRepo(session)


def setup_dependencies(
        app: FastAPI,
        db_session: partial[AsyncGenerator[AsyncSession, None]],
        redis_client: Redis
):
    app.dependency_overrides[get_db_session] = db_session
    app.dependency_overrides[get_redis_client] = lambda: redis_client
    app.dependency_overrides[Stub(MovieRepo)] = get_movie_repo
