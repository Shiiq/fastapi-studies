from dataclasses import dataclass

from fastapi_studies.api.config import ApiConfig
from fastapi_studies.infrastructure.redis.config import RedisConfig


@dataclass
class Config:

    api: ApiConfig
    redis: RedisConfig


def load_config() -> Config:
    return Config(
        api=ApiConfig(),
        redis=RedisConfig()
    )
