from datetime import datetime, timedelta

from jose import JWTError, jwt
from models.user import User
from settings.app_setting import get_app_setting


class TokenUtil:
    def __init__(self) -> None:
        self.__app_settings = get_app_setting()

    def create_access_token(self, user: User):
        claims = {"sub": user.username}

        expire = datetime.utcnow() + timedelta(
            minutes=self.__app_settings.access_token_expire_minutes
        )
        claims.update({"exp": expire})
        encoded_jwt = jwt.encode(
            claims,
            self.__app_settings.secret_key,
            algorithm=self.__app_settings.jwt_algorithm,
        )
        return encoded_jwt

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(
                token,
                self.__app_settings.secret_key,
                algorithms=self.__app_settings.jwt_algorithm,
            )
            username: str = payload.get("sub")
            return username
        except JWTError as e:
            # TODO print to log files
            print(e)
            return None
