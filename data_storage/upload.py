import asyncio
import pathlib

from fastapi_studies.infrastructure.config_loader import load_config
from fastapi_studies.infrastructure.database.connection import create_session_factory
from data_storage.reading import read_csv
from data_storage.inserting import insert_objs

FILEPATH = pathlib.Path("./data_storage/movies.csv")

from sqlalchemy import select, and_
from sqlalchemy.orm import join, joinedload, selectinload
from fastapi_studies.infrastructure.database.models import Genre, Movie, MovieGenre


async def run_upload():
    """Script for upload data to db."""

    data = read_csv(FILEPATH)
    session_factory = create_session_factory(load_config().db)
    async with session_factory() as session:
        await insert_objs(session, data)
        await session.commit()

        # q = select(Movie).limit(10).offset(10)
        # q = select(Movie).where(Movie.year.in_([0, 0]))
        # r = await session.execute(q)
        # r = r.scalars().all()
        # print(len(r))
        # for i in r:
        #     # print(i.id, i.title)
        #     pass

    # await db_engine.dispose()
    #     genres = ["Action", "Animation", "Crime", "Sci-Fi", "Thriller"]
    #     genres = ["Action", "Animation", ]
    #     q = (
    #         select(Movie)
    #         .options(selectinload(Movie.genres))
    #         .where(and_(Movie.genre == genre for genre in genres))
    #         .order_by(
    #             Movie.year.desc(),
    #             Movie.title.asc()
    #         )
    #         .limit(15)
    #         .offset(5)
    #     )
    #     ms = await session.execute(q)
    #     ms = ms.scalars().all()
    #     print(len(ms))
    #     print(15*"-")
    #     for m in ms:
    #         print(m.title, m.genre)


if __name__ == "__main__":
    asyncio.run(run_upload())
