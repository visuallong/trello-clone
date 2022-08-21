import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from config import get_app_setting
from context.db import db_context_middleware, init_db
from routes import auth, boards

app = FastAPI()


app.add_middleware(BaseHTTPMiddleware, dispatch=db_context_middleware)
app.include_router(auth.router)
app.include_router(boards.router)
# use migration tool rather than init all tables
# open this if want to build tables in db during start up
# app.router.on_startup.append(init_db)


@app.get("/", tags=["root"])
async def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app_setting = get_app_setting()
    uvicorn.run(
        "main:app",
        host=app_setting.host,
        port=app_setting.port,
        reload=app_setting.reload,
        debug=app_setting.debug,
    )
