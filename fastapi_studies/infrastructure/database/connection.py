from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from .config import DBConfig


# def create_engine(
#         db_config: DBConfig
# ) -> AsyncEngine:
#     engine = create_async_engine(
#         url=db_config.sqlite_url,
#         echo=db_config.echo
#     )
#     return engine
#
#
# def create_session_factory(
#         engine: AsyncEngine
# ) -> async_sessionmaker:
#     async_session_factory = async_sessionmaker(
#         bind=engine,
#         autoflush=False,
#         expire_on_commit=False
#     )
#     return async_session_factory
#
#
# async def create_db_session(
#         async_session_factory: async_sessionmaker
# ) -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_factory() as session:
#         yield session


def create_session_factory(db_config: DBConfig) -> async_sessionmaker:
    engine = create_async_engine(
        url=db_config.sqlite_url,
        echo=db_config.echo
    )
    return async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )


async def create_db_session(
        async_session_factory: async_sessionmaker
) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

# async def get_db_session(
#         db_config: DBConfig
# ) -> AsyncGenerator[AsyncSession, None]:
#     engine = create_async_engine(
#         url=db_config.sqlite_url,
#         echo=db_config.echo
#     )
#     print(id(engine))
#     session_factory = async_sessionmaker(
#         bind=engine,
#         autoflush=False,
#         expire_on_commit=False
#     )
#     print(id(session_factory))
#     async with session_factory() as session:
#         yield session
