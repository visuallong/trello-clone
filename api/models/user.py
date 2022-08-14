from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from context.db_context import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    hashed_password = Column(String)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
