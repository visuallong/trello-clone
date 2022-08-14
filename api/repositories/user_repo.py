from fastapi import Depends
from sqlalchemy.orm import Session

from context.db_context import get_db
from models.user import User
from schemas.user_dtos import UserCreate
from utils.crypto_utils import CryptoUtil


class UserRepo:
    def __init__(self, db: Session=Depends(get_db), crypto_util: CryptoUtil=Depends(CryptoUtil)) -> None:
        self.__db = db
        self.__crypto_util = crypto_util

    async def get_user(self, username: str) -> User | None:
        return self.__db.query(User).filter(User.username == username).first()

    async def create_user(self,user_create: UserCreate) -> User:
        hashed_password=self.__crypto_util.get_password_hash(user_create.password)
        user = User(username=user_create.username,hashed_password=hashed_password)
        self.__db.add(user)
        self.__db.commit()
        self.__db.refresh(user)
        return user
