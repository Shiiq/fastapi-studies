from typing import AsyncGenerator

from fastapi import FastAPI, Depends
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from .stub import Stub


def get_redis_client() -> Redis:
    raise NotImplementedError


def get_db_session(
        session: AsyncSession = Depends(Stub(AsyncSession))
) -> AsyncSession:
    return session
    # raise NotImplementedError


def setup_dependencies(
        app: FastAPI,
        db_session: AsyncGenerator[AsyncSession, None],
        # db_session,
        redis_client: Redis
):
    # app.dependency_overrides[AsyncSession] = lambda: db_session
    app.dependency_overrides[get_db_session] = lambda: db_session
    # app.dependency_overrides[get_db_session] = get_db_session
    app.dependency_overrides[get_redis_client] = lambda: redis_client
