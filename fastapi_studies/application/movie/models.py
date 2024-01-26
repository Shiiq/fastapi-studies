from dataclasses import dataclass


@dataclass
class Movie:

    title: str
    year: int
    genre: list[str]


@dataclass
class MovieFindData:

    genre: list[str] = None
    year_from: int = 1
    year_to: int = 9999
