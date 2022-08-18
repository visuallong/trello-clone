from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext

from config import get_app_setting
from models.user import User

__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
__app_settings = get_app_setting()


def verfiy_password(plain_password: str, hashed_password: str):
    return __pwd_context.verify(plain_password, hashed_password)


def get_password_hash(plain_password: str):
    return __pwd_context.hash(plain_password)


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
