from functools import partial
from typing import AsyncGenerator

from fastapi import FastAPI, Depends
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_studies.api.dependencies.stub import Stub
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.services import MovieFindService
from fastapi_studies.infrastructure.database.repositories import MovieRepo


def get_redis_client() -> Redis:
    raise NotImplementedError


def get_db_session() -> AsyncSession:
    raise NotImplementedError


def get_movie_repo(
        # session: AsyncSession = Depends(get_db_session),
        session: Stub(AsyncSession) = Depends()
) -> MovieRepo:
    yield MovieRepo(session)


def get_findmovie_service(
        # movie_repo: Stub(MovieRepo) = Depends(),
        movie_repo: Stub(MovieReader) = Depends()
):
    yield MovieFindService(movie_repo)


def setup_dependencies(
        app: FastAPI,
        db_session: partial[AsyncGenerator[AsyncSession, None]],
        redis_client: Redis
):
    # app.dependency_overrides[get_redis_client] = lambda: redis_client
    # app.dependency_overrides[get_db_session] = db_session

    app.dependency_overrides[Stub(Redis)] = lambda: redis_client
    app.dependency_overrides[Stub(AsyncSession)] = db_session
    # app.dependency_overrides[Stub(MovieRepo)] = get_movie_repo
    app.dependency_overrides[Stub(MovieReader)] = get_movie_repo
    app.dependency_overrides[Stub(MovieFindService)] = get_findmovie_service
