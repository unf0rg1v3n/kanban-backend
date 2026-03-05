from myapp.domains.boards.repositories import BoardRepositoryProtocol
from myapp.domains.boards.schemas import BoardCreate
from myapp.db.models import Board
from typing import List, Optional


class BoardService:
    def __init__(self, board_repository: BoardRepositoryProtocol):
        self.board_repository = board_repository
    
    async def create_board(self, board_create: BoardCreate) -> Board:
        return await self.board_repository.create_board(board_create)
    
    async def get_all(self) -> List[Board]:
        return await self.board_repository.list_boards()
    
    async def get_by_id(self, board_id: int) -> Optional[Board]:
        return await self.board_repository.get_board_by_id(board_id)