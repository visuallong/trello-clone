from datetime import datetime, timedelta

from config import get_app_setting
from jose import JWTError, jwt
from models import User

__app_settings = get_app_setting()


def create_access_token(user: User):
    # TODO add roles
    claims = {"sub": user.username}

    expire = datetime.utcnow() + timedelta(
        minutes=__app_settings.access_token_expire_minutes
    )
    claims.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims,
        __app_settings.secret_key,
        algorithm=__app_settings.jwt_algorithm,
    )
    return encoded_jwt


def decode_token(token: str):
    try:
        payload = jwt.decode(
            token,
            __app_settings.secret_key,
            algorithms=__app_settings.jwt_algorithm,
        )
        username: str = payload.get("sub")
        return username
    except JWTError as e:
        # TODO print to log files
        print(e)
        return None
