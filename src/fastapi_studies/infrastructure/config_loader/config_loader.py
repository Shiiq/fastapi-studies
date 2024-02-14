from dataclasses import dataclass

from fastapi_studies.api.config import ApiConfig
from fastapi_studies.infrastructure.database.config import DBConfig
from fastapi_studies.infrastructure.redis.config import RedisConfig


@dataclass(frozen=True, slots=True)
class Config:

    api: ApiConfig
    db: DBConfig
    redis: RedisConfig


def load_config() -> Config:
    return Config(
        api=ApiConfig(),
        db=DBConfig(),
        redis=RedisConfig()
    )
