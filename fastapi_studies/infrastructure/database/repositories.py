from typing import Sequence

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.infrastructure.database.models import Movie


class MovieRepo(MovieReader):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_movies_by_genre_and_year(
            self,
            filter_data,
    ) -> Sequence[Movie]:
        q = (
            select(Movie)
            .options(selectinload(Movie.genres))
            .where(and_(Movie.genre == genre for genre in filter_data.genre))
            .where(Movie.year.between(filter_data.year_from, filter_data.year_to))
            .order_by(Movie.year.desc(), Movie.title.asc())
        )
        movies = await self._session.execute(q)
        movies = movies.scalars().all()
        return movies
