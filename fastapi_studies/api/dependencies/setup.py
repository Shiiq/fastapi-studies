from fastapi import FastAPI
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession


def get_redis_client() -> Redis:
    raise NotImplementedError


def get_db_session() -> AsyncSession:
    raise NotImplementedError


def setup_dependencies(app: FastAPI, redis_client: Redis):
    app.dependency_overrides[get_redis_client] = lambda: redis_client
