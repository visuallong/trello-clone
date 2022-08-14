from fastapi import FastAPI, HTTPException, status, Depends
from dtos import LoginModel, RegisterModel
from utils import create_access_token, get_current_user, get_user, verfiy_password
from settings import get_app_settings
import uvicorn

app = FastAPI()
app_settings = get_app_settings()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post("/api/auth/signup")
async def signup(register_model: RegisterModel):
    pass


@app.post("/api/auth/login")
async def login(login_model: LoginModel):
    user = get_user(login_model.username)

    if not user or (
        user and not verfiy_password(login_model.password, user["password"])
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="username or password incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"token": create_access_token(user), "token_type": "bearer"}


@app.get("/api/boards")
async def get_user_board(current_user=Depends(get_current_user)):
    return {"user board": "TODO"}


if __name__ == "__main__":
    if app_settings.env == "dev":
        uvicorn.run(
            "main:app",
            host=app_settings.app_host,
            port=app_settings.app_port,
            reload=True,
            debug=True,
            workers=3,
        )
    elif app_settings.env == "prod":
        # TODO
        print("app running at *:3000")
