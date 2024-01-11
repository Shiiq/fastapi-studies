from functools import partial

from fastapi_studies.api.app import create_app
from fastapi_studies.infrastructure.config_loader import load_config
# from fastapi_studies.infrastructure.database.connection import get_db_session
from fastapi_studies.infrastructure.database.connection import create_session_factory
from fastapi_studies.infrastructure.database.connection import create_db_session
from fastapi_studies.infrastructure.redis.client import get_redis_client


def initialize_application():

    config = load_config()
    # db_session = get_db_session(config.db)
    session_factory = create_session_factory(config.db)
    db_session = create_db_session(session_factory)
    # db_session = partial(create_db_session, session_factory)
    redis_client = get_redis_client(config.redis)

    return create_app(config.api, db_session, redis_client)


app = initialize_application()
