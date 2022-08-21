from enum import unique
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from context.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    # email = Column(String, index=True, unique=True, nullable=False)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    hashed_password = Column(String, nullable=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    create_date = Column(DateTime(timezone=True), server_default=func.now())

# TODO
# class UserRole(Base):
#     __tablename__ = "users_roles"

class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    # TODO add 1 or more list relationship
