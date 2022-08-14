from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from repositories.user_repo import UserRepo
from utils.token_utils import TokenUtil

__scheme = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(__scheme),
    user_repo: UserRepo = Depends(UserRepo),
    token_util: TokenUtil = Depends(TokenUtil),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = token_util.decode_token(credentials.credentials)
    if not username:
        raise credentials_exception
    user = await user_repo.get_user(username=username)
    if not user:
        raise credentials_exception
    return user
