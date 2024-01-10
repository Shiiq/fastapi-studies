from contextlib import asynccontextmanager
from functools import partial
from typing import AsyncContextManager

from fastapi import FastAPI
from redis.asyncio.client import Redis

from fastapi_studies.api.dependencies.setup import setup_dependencies
from fastapi_studies.api.routers.setup import setup_routers
from .config import ApiConfig


@asynccontextmanager
async def dependencies_lifespan(app: FastAPI,
                                redis_client_source: AsyncContextManager[Redis]):
    async with redis_client_source as redis_client:
        setup_dependencies(app, redis_client)
        yield


def create_app(
        api_config: ApiConfig,
        redis_client_source: AsyncContextManager[Redis]
) -> FastAPI:
    lifespan = partial(
        dependencies_lifespan,
        redis_client_source=redis_client_source
    )
    app = FastAPI(
        title=api_config.title,
        lifespan=lifespan
    )
    setup_routers(app)
    return app
