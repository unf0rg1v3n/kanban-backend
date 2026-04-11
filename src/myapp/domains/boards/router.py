from fastapi import APIRouter, Query, Path, Header, HTTPException, Depends
from myapp.db.core import SessionDep
from myapp.domains.boards.service import BoardService
from myapp.domains.boards.schemas import BoardRead, BoardCreate
from myapp.domains.boards.repositories import PostgresBoardRepository
from typing import List


def get_board_service(session: SessionDep) -> BoardService:
    return BoardService(PostgresBoardRepository(session))


router = APIRouter(prefix="/boards", tags=["boards"])

@router.post("/", response_model=BoardRead, summary="Create a new board")
async def create_board(board_create: BoardCreate, 
                       service: BoardService = Depends(get_board_service)):
    return await service.create_board(board_create)


@router.get("/", response_model=List[BoardRead])
async def get_board(service: BoardService = Depends(get_board_service)):
    return await service.get_all()


@router.get("/{board_id}", response_model=BoardRead)
async def get_board_by_id(board_id: int,
                          service: BoardService = Depends(get_board_service)):
    board = await service.get_by_id(board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return board
