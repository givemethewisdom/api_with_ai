"""Gloval config"""
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = "mydbuser"
    DB_PASSWORD: str = "mydbpass"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "mydb"


    @property
    #пока не проверенный url
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
