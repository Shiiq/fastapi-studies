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


def get_g(param):
    return Genre(param)


if __name__ == "__main__":
    d = {
        "dep_1": {},
    }
    # first request to private obj
    print(d["dep_1"].get("user_1", False))

    # some authentication
    # result is
    d["dep_1"]["user_1"] = True
    print(d)

    d["dep_1"].setdefault("user_1", False)
    print(d)

    d["dep_2"] = {}
    print(d)

    d["dep_2"].setdefault("user_2", False)
    print(d)

    d["dep_2"].setdefault("user_2", True)
    print(d)

    pass
