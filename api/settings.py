from pydantic import BaseSettings


class AppSettings(BaseSettings):
    env: str

    class Config:
        env_file: str = ".env"
