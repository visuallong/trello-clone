from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings.app_setting import get_app_setting

__app_settings = get_app_setting()

engine = create_engine(__app_settings.db_url)

__SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = __SessionLocal()
        yield db
    finally:
        db.close()
