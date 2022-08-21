from pydantic import BaseModel


class __UserBase(BaseModel):
    username: str


class UserCreate(__UserBase):
    password: str


class UserLogin(__UserBase):
    password: str
