from typing import Sequence

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_studies.infrastructure.database.models import Genre, Movie


class SQLAlchemyRepo:

    _session: AsyncSession

    def __init__(self, session: AsyncSession):
        self._session = session


class MovieRepo(SQLAlchemyRepo):

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_genre(self, genres: list[Genre]) -> Sequence[Movie]:
        q = (
            select(Movie)
            .options(selectinload(Movie.genres))
            .where(and_(Movie.genre == genre for genre in genres))
            .order_by(Movie.year.desc(), Movie.title.asc())
        )
        movies = await self._session.execute(q)
        movies = movies.scalars().all()
        return movies
