import asyncio
import pathlib

from fastapi_studies.infrastructure.config_loader import load_config
from fastapi_studies.infrastructure.database.connection import create_session_factory
from data_storage.reading import read_csv
from data_storage.inserting import insert_objs

FILEPATH = pathlib.Path("./data_storage/movies.csv")


async def run_upload():
    """Script for upload data to db."""

    data = read_csv(FILEPATH)
    session_factory = create_session_factory(load_config().db)
    async with session_factory() as session:
        await insert_objs(session, data)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(run_upload())
