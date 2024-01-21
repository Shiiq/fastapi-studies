from dataclasses import dataclass


@dataclass
class Movie:

    title: str
    year: int
    genre: list[str]
