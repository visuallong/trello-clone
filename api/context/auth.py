from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from repos.users import UserRepo
from services.token import decode_token


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    user_repo: UserRepo = Depends(UserRepo),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = decode_token(credentials.credentials)
    if not username:
        raise credentials_exception
    user = await user_repo.get_user(username=username)
    if not user:
        raise credentials_exception
    return user
