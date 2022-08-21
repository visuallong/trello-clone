from typing import List
from context.db import get_db_session
from fastapi import Depends
from models import Board
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class BoardRepo:
    def __init__(
        self,
        db_context: Session = Depends(get_db_session),
    ) -> None:
        self.__db_context = db_context

    async def get_board(self, board_name: str) -> Board | None:
        result = await self.__db_context.execute(
            select(Board).where(Board.name == board_name)
        )
        return result.scalars().first()

    async def get_boards(self) -> List[Board]:
        result = await self.__db_context.execute(select(Board))
        return result.scalars().all()

    async def create_board(self, board: Board) -> Board:
        self.__db_context.add(board)
        await self.__db_context.commit()
        return board
