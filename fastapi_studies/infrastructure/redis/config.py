from dataclasses import dataclass


@dataclass
class RedisConfig:

    host: str = "localhost"
    port: int = 6379
