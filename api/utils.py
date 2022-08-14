from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from jose import jwt, JWTError
from settings import get_app_settings

# Mock db
db = {"bob": {"username": "bob", "password": "abc"}}

app_settings = get_app_settings()
scheme = HTTPBearer()


def verfiy_password(plain_password: str, hashed_password: str):
    # TODO use bcrypt
    return plain_password == hashed_password


def get_password_hash(password: str):
    # TODO hash password
    return password


def get_user(username: str):
    if username in db:
        return db[username]
    return None


def create_access_token(user):
    claims = {"username": user["username"]}

    expire = datetime.utcnow() + timedelta(
        minutes=app_settings.access_token_expire_minutes
    )
    claims.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims, app_settings.secret_key, algorithm=app_settings.jwt_algorithm
    )
    return encoded_jwt


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = credentials.credentials
        payload = jwt.decode(
            token, app_settings.secret_key, algorithms=app_settings.jwt_algorithm
        )
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError as e:
        print(e)
        raise credentials_exception
    user = get_user(username=username)
    if user is None:
        raise credentials_exception
    return user
