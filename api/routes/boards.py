from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from models import Board
from repos.boards import BoardRepo
from schemas.boards import CreateBoard
from schemas.paginated import PaginatedRequest

router = APIRouter(
    prefix="/api/boards", tags=["boards"], dependencies=[Depends(HTTPBearer())]
)


@router.get("/")
async def get_boards(
    board_repo: BoardRepo = Depends(BoardRepo),
    paginated_request: PaginatedRequest = Depends(),
):
    boards = await board_repo.get_boards()
    return boards


@router.post("/")
async def create_board(
    create_board: CreateBoard, board_repo: BoardRepo = Depends(BoardRepo)
):
    board = await board_repo.get_board(create_board.name.strip())
    if board:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="board exists"
        )

    board = Board(name=create_board.name)
    board = await board_repo.create_board(board)
    return board
