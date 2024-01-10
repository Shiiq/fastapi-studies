from dataclasses import dataclass


@dataclass
class DBConfig:

    db_url: str = "./fastapi_studies.db"
    echo: bool = False

    @property
    def sqlite_url(self):
        """SQLITE database url"""
        return f"sqlite+aiosqlite:///./{self.db_url}"
