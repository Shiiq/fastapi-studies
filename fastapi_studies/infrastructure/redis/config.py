from dataclasses import dataclass


@dataclass
class RedisConfig:

    host: str = "cache"
    port: int = 6379
