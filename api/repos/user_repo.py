from db import get_db_session
from fastapi import Depends
from models.user import User
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class UserRepo:
    def __init__(
        self,
        db_context: Session = Depends(get_db_session),
    ) -> None:
        self.__db_context = db_context

    async def get_user(self, username: str) -> User | None:
        result = await self.__db_context.execute(
            select(User).where(User.username == username)
        )
        return result.scalars().first()

    async def create_user(self, user: User) -> User:
        self.__db_context.add(user)
        await self.__db_context.flush()
        return user
