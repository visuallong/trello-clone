from fastapi import Request, Response, status
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_app_setting

# https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html

__app_settings = get_app_setting()

__engine = create_async_engine(
    __app_settings.db_url, future=True, echo=__app_settings.show_sql
)

__async_session = sessionmaker(
    bind=__engine, expire_on_commit=False, class_=AsyncSession
)

Base = declarative_base()


async def db_context_middleware(request: Request, call_next):
    response = Response(
        "Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    try:
        request.state.db = __async_session()
        request.state.db.begin()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


def get_db_session(request: Request):
    return request.state.db


async def init_db():
    # create db tables
    async with __engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
