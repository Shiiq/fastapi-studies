from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_studies.infrastructure.database.models import Genre, Movie
from .reading import GENRES, TITLE, YEAR


async def insert_objs(
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
