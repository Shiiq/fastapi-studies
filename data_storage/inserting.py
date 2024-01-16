import asyncio
import pathlib
from typing import Iterable

from sqlalchemy import bindparam, select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_studies.infrastructure.config_loader import load_config
from fastapi_studies.infrastructure.database.connection import create_engine
from fastapi_studies.infrastructure.database.connection import create_session_factory
from fastapi_studies.infrastructure.database.models import Genre, Movie
from data_storage.reading import read_csv

FILEPATH = pathlib.Path("./data_storage/movies.csv")
TITLE = "title"
YEAR = "year"
GENRES = "genres"


async def _insert_objs(
        session: AsyncSession,
        data: Iterable[dict[str, str]]
):
    genres = {}

    for chunk in data:
        session.add(
            Movie(
                title=chunk[TITLE],
                year=chunk[YEAR],
                genres=[genres.setdefault(genre_name, Genre(name=genre_name))
                        for genre_name in chunk[GENRES]]
            )
        )

    del genres

    # await db_conn.execute(
    #     insert(Movie)
    #     .values([line for line in data])
    #     .on_conflict_do_nothing()
    # )


async def run_insert():

    data = read_csv(FILEPATH)
    session_factory = create_session_factory(load_config().db)
    async with session_factory() as session:
        await _insert_objs(session, data)
        await session.commit()

    # db_engine = create_engine(load_config().db)
    # async with db_engine.begin() as db_conn:
    #     await _insert_stmt(db_conn, data)
    #
    # await db_engine.dispose()


if __name__ == "__main__":
    asyncio.run(run_insert())
