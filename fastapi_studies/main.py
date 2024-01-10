from fastapi_studies.api.app import create_app
from fastapi_studies.infrastructure.config_loader import load_config
from fastapi_studies.infrastructure.redis.client import get_redis_client


def initialize_application():
    config = load_config()
    redis_client = get_redis_client(config.redis)
    app = create_app(config.api, redis_client)
    return app


app = initialize_application()
