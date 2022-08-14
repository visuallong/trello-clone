import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status

from context.db_context import engine, Base
from context.user_auth import get_current_user
from repositories.user_repo import UserRepo
from schemas.user_dtos import UserCreate, UserLogin
from settings.app_setting import get_app_setting
from utils.crypto_utils import CryptoUtil
from utils.token_utils import TokenUtil

app = FastAPI()
__app_setting = get_app_setting()

Base.metadata.create_all(bind=engine)


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post("/api/auth/signup")
async def signup(
    user_create: UserCreate,
    user_repo: UserRepo = Depends(UserRepo),
    token_util: TokenUtil = Depends(TokenUtil),
):
    if await user_repo.get_user(user_create.username.strip()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user exists"
        )

    user = await user_repo.create_user(user_create)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong. Please try again",
        )

    return {"access_token": token_util.create_access_token(user)}


@app.post("/api/auth/login")
async def login(
    user_login: UserLogin,
    user_repo: UserRepo = Depends(UserRepo),
    token_util: TokenUtil = Depends(TokenUtil),
    crypto_util: CryptoUtil = Depends(CryptoUtil),
):
    user = await user_repo.get_user(user_login.username)

    if not user or (
        user
        and not crypto_util.verfiy_password(user_login.password, user.hashed_password)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="username or password incorrect",
        )

    return {"access_token": token_util.create_access_token(user)}


@app.get("/api/boards")
async def get_user_board(current_user=Depends(get_current_user)):
    return {"user board": "TODO"}


if __name__ == "__main__":
    if __app_setting.env == "dev":
        uvicorn.run(
            "main:app",
            host="localhost",
            port=__app_setting.app_dev_port,
            reload=True,
            debug=True,
            workers=3,
        )
    elif __app_setting.env == "prod":
        # TODO
        print("app running at *:3000")
