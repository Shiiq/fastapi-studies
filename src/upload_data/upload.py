import pathlib
from sys import stdout

from sqlalchemy.exc import IntegrityError

from fastapi_studies.infrastructure.config_loader import load_config
from fastapi_studies.infrastructure.database.connection import create_session_factory
from upload_data.reading import read_csv
from upload_data.inserting import insert_objs

FILEPATH = pathlib.Path("./data/movies.csv")


async def run_upload():
    """Script for upload data to db"""
    stdout.write("\nPreparing to upload data to the database\n")

    data = read_csv(FILEPATH)
    session_factory = create_session_factory(load_config().db)
    async with session_factory() as session:
        insert_objs(session, data)
        try:
            await session.commit()
        except IntegrityError:
            pass

    stdout.write(
        f"\nThe data from the <{FILEPATH}>"
        f" has been successfully uploaded to the database\n"
    )
