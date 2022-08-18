from functools import lru_cache

from pydantic import BaseSettings


@lru_cache()
def get_app_setting():
    """
    Get app settings from Environment variables
    check more at https://fastapi.tiangolo.com/advanced/settings/#creating-the-settings-only-once-with-lru_cache
    """
    return __AppSetting()


class __AppSetting(BaseSettings):
    host: str | None = "127.0.0.1"
    port: int | None = 7000
    secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int
    db_url: str
    reload: bool | None = False
    debug: bool | None = False
    show_sql: bool | None = False

    class Config:
        env_file: str = ".env"
