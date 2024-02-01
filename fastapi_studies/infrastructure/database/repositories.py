from typing import Iterator

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_studies.application.movie.interfaces import MovieReader
from fastapi_studies.application.movie.models import Movie as MovieDTO
from fastapi_studies.application.movie.models import MovieFilterParams
from fastapi_studies.infrastructure.database.models import Movie as MovieORM


def movie_orm_to_dto(input_data: MovieORM) -> MovieDTO:
    return MovieDTO(
        title=input_data.title,
        year=input_data.year,
        genres=list(input_data.genre)
    )


class MovieDBRepo(MovieReader):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_genre_and_year(
            self,
            filter_params: MovieFilterParams,
    ) -> Iterator[MovieDTO]:
        q = (
            select(MovieORM)
            .options(selectinload(MovieORM.genres))
            .where(MovieORM.year.between(
                filter_params.year_from,
                filter_params.year_to))
            .order_by(MovieORM.year.desc(), MovieORM.title.asc())
        )
        if filter_params.genre:
            q = q.where(and_(
                MovieORM.genre == genre for genre in filter_params.genre
            ))

        movies = await self._session.execute(q)
        movies = movies.scalars().all()
        return map(movie_orm_to_dto, movies)
