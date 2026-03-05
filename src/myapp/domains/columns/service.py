from typing import List
from myapp.db.models import BoardColumn
from myapp.domains.columns.repositories import ColumnRepositoryProtocol
from myapp.domains.columns.schemas import ColumnCreate


class ColumnService:
    def __init__(self, column_repository: ColumnRepositoryProtocol):
        self.column_repository = column_repository
    
    async def create_column(self, board_id: int, column_create: ColumnCreate) -> BoardColumn:
        return await self.column_repository.create_column(board_id, column_create)
    
    async def get_columns(self, board_id: int) -> List[BoardColumn]:
        return await self.column_repository.get_columns(board_id)