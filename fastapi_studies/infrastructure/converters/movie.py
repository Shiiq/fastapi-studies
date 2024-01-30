from dataclasses import asdict
from json import dumps, loads

from fastapi_studies.application.movie.models import Movie as MovieDTO
from fastapi_studies.infrastructure.database.models import Movie as MovieORM


def movie_dto_to_json(input_data: MovieDTO) -> str:
    movie_as_dict = asdict(input_data)
    return dumps(movie_as_dict)


def movie_json_to_dto(input_data: str) -> MovieDTO:
    movie_as_dict = loads(input_data)
    return MovieDTO(
        title=movie_as_dict["title"],
        year=int(movie_as_dict["year"]),
        genres=movie_as_dict["genres"]
    )


def movie_orm_to_dto(input_data: MovieORM) -> MovieDTO:
    return MovieDTO(
        title=input_data.title,
        year=input_data.year,
        genres=list(input_data.genre)
    )
