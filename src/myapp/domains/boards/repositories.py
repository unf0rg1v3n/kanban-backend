from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from myapp.db.models import Board
from myapp.domains.boards.schemas import BoardCreate, BoardCreate
from typing import Protocol, Optional, List


class BoardRepositoryProtocol(Protocol):
    async def create_board(self, board_create: BoardCreate) -> Board:
        ...

    async def get_board_by_id(self, board_id: int) -> Optional[Board]:
        ...

    async def list_boards(self) -> List[Board]:
        ...


class PostgresBoardRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_board(self, board_create: BoardCreate) -> Board:
        new_board = Board(title=board_create.title)
        self.session.add(new_board)
        await self.session.commit()
        await self.session.refresh(new_board)
        return new_board
    
    async def get_board_by_id(self, board_id: int) -> Optional[Board]:
        board = await self.session.get(Board, board_id)
        return board
    
    async def list_boards(self) -> List[Board]:
        result = await self.session.scalars(select(Board))
        return list(result.all())