from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_studies.infrastructure.database.models import Genre, Movie
from .reading import GENRES, TITLE, YEAR


def insert_objs(
        session: AsyncSession,
        data: Iterable[dict[str, str]]
):

    genres: dict[str, Genre] = {}
    for chunk in data:
        session.add(
            Movie(
                title=chunk[TITLE],
                year=chunk[YEAR],
                genres=[
                    genres.setdefault(genre_name, Genre(name=genre_name))
                    for genre_name in chunk[GENRES]
                ]
            )
        )

    del genres
