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
    env: str
    secret_key: str
    jwt_algorithm: str
    app_dev_port: int
    access_token_expire_minutes: int
    db_url: str

    class Config:
        env_file: str = ".env"
    