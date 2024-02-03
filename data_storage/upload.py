import asyncio
import pathlib
import sys
from sys import stdout

from sqlalchemy.exc import IntegrityError

from fastapi_studies.infrastructure.config_loader import load_config
from fastapi_studies.infrastructure.database.connection import create_session_factory
from data_storage.reading import read_csv
from data_storage.inserting import insert_objs

FILEPATH = pathlib.Path("./data_storage/movies.csv")


async def run_upload():
    """Script for upload data to db"""

    data = read_csv(FILEPATH)
    session_factory = create_session_factory(load_config().db)
    async with session_factory() as session:
        await insert_objs(session, data)
        await session.commit()

    stdout.write(
        f"\nThe data from the <{FILEPATH}>"
        f" has been successfully uploaded to the database\n"
    )


if __name__ == "__main__":
    asyncio.run(run_upload())
