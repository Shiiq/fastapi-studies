from functools import partial
from typing import AsyncGenerator

from fastapi import FastAPI
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession


def get_redis_client() -> Redis:
    raise NotImplementedError


def get_db_session() -> AsyncSession:
    raise NotImplementedError


def setup_dependencies(
        app: FastAPI,
        db_session: partial[AsyncGenerator[AsyncSession, None]],
        redis_client: Redis
):
    app.dependency_overrides[get_db_session] = db_session
    app.dependency_overrides[get_redis_client] = lambda: redis_client
