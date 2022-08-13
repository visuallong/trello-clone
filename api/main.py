from fastapi import FastAPI
from functools import lru_cache
from settings import AppSettings
import uvicorn

app = FastAPI()


@lru_cache()
def get_settings():
    return AppSettings()


@app.get("/")
async def index():
    return {"message": "Hello World"}


if __name__ == '__main__':
    if get_settings().env == "dev":
        uvicorn.run("main:app", host="localhost", port=3000,
                    reload=True, debug=True, workers=3)
    elif get_settings().env == "prod":
        # TODO
        print("app running at *:3000")