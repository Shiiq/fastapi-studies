import asyncio
import pathlib
from typing import Iterable

from sqlalchemy import bindparam, select
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.asyncio import AsyncConnection

from fastapi_studies.infrastructure.config_loader import load_config
from fastapi_studies.infrastructure.database.connection import create_engine
from fastapi_studies.infrastructure.database.models import Movie, Genre
from data_storage.reading import read_csv

FILEPATH = pathlib.Path("./data_storage/movies.csv")


async def _insert_stmt(
        db_conn: AsyncConnection,
        data: Iterable[dict[str, str]]
):
    await db_conn.execute(
        insert(Movie)
        .values([line for line in data])
        .on_conflict_do_nothing()
    )


async def run_insert():
    data = read_csv(FILEPATH)
    db_engine = create_engine(load_config().db)
    async with db_engine.begin() as db_conn:
        await _insert_stmt(db_conn, data)

    await db_engine.dispose()
    # genres = [
    #     {"name": "comedy"},
    #     {"name": "drama"},
    #     {"name": "thriller"},
    #     {"name": "crime"}
    # ]
    # movies = [
    #     {"title": "good", "year": 1990, "genres": ["comedy", ]},
    #     {"title": "bad", "year": 2000, "genres": ["drama", "thriller"]},
    #     {"title": "ugly", "year": 2010, "genres": ["drama", "thriller", "crime"]},
    # ]
    # scalar_subquery = (
    #     select(Genre.id)
    #     .where(Genre.name == bindparam("genres"))
    #     .scalar_subquery()
    # )
    # async with db_engine.begin() as db_conn:
    #     await db_conn.execute(
    #         # insert(Genre)
    #         # .values(genres)
    #         # .on_conflict_do_nothing()
    #         # insert(Movie)
    #         # .values(movies)
    #         # .on_conflict_do_nothing()
    #         insert(Movie)
    #         .values(genres=scalar_subquery),
    #         movies
    #     )


if __name__ == "__main__":
    asyncio.run(run_insert())
