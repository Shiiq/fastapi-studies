from typing import Sequence

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_studies.application.movie.models import MovieFilterData
from fastapi_studies.application.movie.models import MoviePagination
from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.infrastructure.database.models import Movie


class MovieRepo(MovieReader):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_genre_and_year(
            self,
            filter_params: MovieFilterData,
            pagination_params: MoviePagination | None = None,
    ) -> Sequence[Movie]:
        q = (
            select(Movie)
            .options(selectinload(Movie.genres))
            .where(Movie.year.between(
                filter_params.year_from,
                filter_params.year_to))
            .order_by(Movie.year.desc(), Movie.title.asc())
        )
        if filter_params.genre:
            q = q.where(and_(
                Movie.genre == genre for genre in filter_params.genre
            ))
        if pagination_params:
            q = q.limit(pagination_params.limit)
            q = q.offset(pagination_params.offset)

        movies = await self._session.execute(q)
        movies = movies.scalars().all()
        return movies
