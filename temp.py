import asyncio
import csv
import datetime
from contextlib import asynccontextmanager
from typing import AsyncGenerator


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


if __name__ == "__main__":
    # with open("movies.csv", newline="") as f:
    #     reader = csv.reader(f, delimiter=",")
    #     header = next(reader)
    #     for r in reader:
    #         print(r[0], r[1])
    # asyncio.run(type_checker())
    # res = main()
    # print(f"THE END OF ANYTHING, special_msg: {res}")
    x = "Action|Animation|Crime|Sci-Fi|Thriller"
    x = x.split("|")
    dct = {}
    # print([dct.get(g_name, Genre(name=g_name)) for g_name in x])
    # print(dct)
    # print([dct.setdefault(g_name, Genre(name=g_name)) for g_name in x])
    # print(dct)
    pass
