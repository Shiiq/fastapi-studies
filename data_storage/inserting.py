from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.sqlite import insert as sqlite_upsert

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
                genres=[genres.setdefault(genre_name.lower(), Genre(name=genre_name.lower()))
                        for genre_name in chunk[GENRES]]
            )
        )

    del genres
