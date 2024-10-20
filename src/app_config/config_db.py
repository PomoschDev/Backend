from functools import cached_property
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_prefix="DB__",
        env_file=".env",
        extra="ignore",
    )
    HOST: str
    PORT: str
    USER: str
    PASS: str

    @cached_property
    def db_settings(self):
        return self

    @cached_property
    def dsn_async(self):
        # Используется для gRPC
        return (
            f"grpc+async://{self.USER}:{self.PASS}"
            f"@{self.HOST}:{self.PORT}"
        )

    @cached_property
    def dsn_sync(self):
        # Если потребуется синхронное подключение, можно добавить
        return (
            f"grpc://{self.USER}:{self.PASS}"
            f"@{self.HOST}:{self.PORT}"
        )


class TestDBSettings(BaseSettings):
    NAME: str = "test_db.db"
    USER: str = ""
    PASS: str = ""

    @computed_field(return_type=str)
    def dsn_async(self):
        return f"sqlite+aiosqlite:///{self.NAME}"

    @computed_field(return_type=str)
    def dsn_sync(self):
        return f"sqlite:///{self.NAME}"


db_settings = DBSettings()
test_db_settings = TestDBSettings()
