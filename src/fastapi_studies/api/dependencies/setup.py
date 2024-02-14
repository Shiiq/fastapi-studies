from functools import partial
from typing import AsyncGenerator, Generator

from fastapi import FastAPI, Depends
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_studies.api.dependencies.stub import Stub
from fastapi_studies.application.movie.interfaces import MovieCache
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.services import MovieFindService
from fastapi_studies.infrastructure.database.repositories import MovieDBRepo
from fastapi_studies.infrastructure.redis.repositories import MovieCacheRepo


def get_cache_repo(
        redis_client: Stub(Redis) = Depends()
) -> Generator[MovieCacheRepo, None, None]:
    yield MovieCacheRepo(redis_client)


def get_db_repo(
        session: Stub(AsyncSession) = Depends()
) -> Generator[MovieDBRepo, None, None]:
    yield MovieDBRepo(session)


def get_moviefind_service(
        movie_cache_repo: Stub(MovieCache) = Depends(),
        movie_db_repo: Stub(MovieReader) = Depends()
) -> Generator[MovieFindService, None, None]:
    yield MovieFindService(movie_cache_repo, movie_db_repo)


def setup_dependencies(
        app: FastAPI,
        db_session: partial[AsyncGenerator[AsyncSession, None]],
        redis_client: Redis
):
    app.dependency_overrides[Stub(AsyncSession)] = db_session
    app.dependency_overrides[Stub(Redis)] = lambda: redis_client
    app.dependency_overrides[Stub(MovieCache)] = get_cache_repo
    app.dependency_overrides[Stub(MovieReader)] = get_db_repo
    app.dependency_overrides[Stub(MovieFindService)] = get_moviefind_service
