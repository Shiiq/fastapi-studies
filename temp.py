import asyncio
import csv
import datetime
import json
from dataclasses import asdict, dataclass, Field
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from pydantic import BaseModel


# @asynccontextmanager
async def get_some_connection() -> AsyncGenerator[str, None]:
    connection = "connection"
    print("yielding conn")
    yield connection
    print("closing conn")


async def type_checker():
    print(type(get_some_connection()))
    async with get_some_connection() as conn:
        print(type(conn))


class CM:

    param_1: str = "SETUP redis connection"
    param_2: str = "CLOSING redis connection"

    def __enter__(self):
        print(f"ENTERING INTO, special_msg: {self.param_1}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"EXITING from, special_msg: {self.param_2}")


def main():
    cm = CM()
    with cm:
        print("APPLICATION MAIN LOGIC")
        return 1000


class Genre:
    def __init__(self, name):
        self.name = name


def get_g(param):
    return Genre(param)


@dataclass
class MovieFilterData:

    genre: list[str] | None
    year_from: int
    year_to: int




if __name__ == "__main__":
    # i = "Action|Adventure|Animation|Children|Comedy"
    # print(i.lower().split("|"))
    mf = MovieFilterData(
        # genre=['comedy', ],
        genre=['comedy', 'action', 'adventure', 'animation', 'children'],
        # genre=None,
        year_from=2006,
        year_to=2007
    )
    d = [
        [],
        ['comedy', ],
        ['comedy', 'action', 'adventure', 'animation', 'children'],
        None,
    ]
    def res(data):
        return f"movies:{('-').join(data) if data else 'all'}"
    # res = f"movies:{('-').join(mf.genre) if mf.genre else 'all'}"
    for data in d:
        print(res(data))


    pass
