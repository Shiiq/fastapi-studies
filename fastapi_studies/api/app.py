from contextlib import asynccontextmanager
from functools import partial
from typing import AsyncContextManager, AsyncGenerator

from fastapi import FastAPI
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_studies.api.dependencies import setup_dependencies
from fastapi_studies.api.exception_handlers import setup_exception_handlers
from fastapi_studies.api.routers import setup_routers
from .config import ApiConfig


@asynccontextmanager
async def dependencies_lifespan(
        app: FastAPI,
        db_session_source: partial[AsyncGenerator[AsyncSession, None]],
        redis_client_source: AsyncContextManager[Redis]
):
    async with redis_client_source as redis_client:
        setup_dependencies(app, db_session_source, redis_client)
        yield


def create_app(
        api_config: ApiConfig,
        db_session_source: partial[AsyncGenerator[AsyncSession, None]],
        redis_client_source: AsyncContextManager[Redis]
) -> FastAPI:
    lifespan = partial(
        dependencies_lifespan,
        db_session_source=db_session_source,
        redis_client_source=redis_client_source
    )
    app = FastAPI(title=api_config.title, lifespan=lifespan)
    setup_exception_handlers(app)
    setup_routers(app)
    return app
