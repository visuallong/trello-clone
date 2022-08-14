from functools import lru_cache
from pydantic import BaseSettings


@lru_cache()
def get_app_settings():
    """
    Get app settings from Environment variables
    check more at https://fastapi.tiangolo.com/advanced/settings/#creating-the-settings-only-once-with-lru_cache
    """
    return AppSettings()


class AppSettings(BaseSettings):
    env: str
    secret_key: str
    jwt_algorithm: str
    app_host: str
    app_port: int
    access_token_expire_minutes: int

    class Config:
        env_file: str = ".env"
