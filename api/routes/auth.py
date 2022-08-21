from fastapi import APIRouter, Depends, HTTPException, status
from models import User
from repos.users import UserRepo
from schemas.users import UserCreate, UserLogin
from services.crypto import get_password_hash, verfiy_password
from services.token import create_access_token

router = APIRouter(
    prefix="/api/auth",
    tags=["authentication"],
)


@router.post("/signup")
async def signup(user_create: UserCreate, user_repo: UserRepo = Depends(UserRepo)):
    if await user_repo.get_user(user_create.username.strip()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user exists"
        )

    user = await user_repo.create_user(__create_user(user_create))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Please try again",
        )

    return {"access_token": create_access_token(user)}


@router.post("/login")
async def login(user_login: UserLogin, user_repo: UserRepo = Depends(UserRepo)):
    user = await user_repo.get_user(user_login.username)

    if not user or (
        user and not verfiy_password(user_login.password, user.hashed_password)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="username or password incorrect",
        )

    return {"access_token": create_access_token(user)}


def __create_user(user_create: UserCreate):
    hashed_password = get_password_hash(user_create.password)
    return User(username=user_create.username.strip(), hashed_password=hashed_password)
