from typing import Protocol, List
from myapp.db.models import BoardColumn
from myapp.domains.columns.schemas import ColumnCreate, ColumnRead
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ColumnRepositoryProtocol(Protocol):
    async def create_column(self, board_id: int, column: ColumnCreate) -> BoardColumn:
        ...

    async def get_columns(self, board_id: int) -> List[BoardColumn]:
        ...


class PostgresColumnRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_column(self, board_id: int, column: ColumnCreate) -> BoardColumn:
        new_column = BoardColumn(board_id=board_id, title=column.title, 
                                 color=column.color, position=column.position)
        self.session.add(new_column)
        await self.session.commit()
        await self.session.refresh(new_column)
        return new_column
    
    async def get_columns(self, board_id: int) -> List[BoardColumn]:
        result = await self.session.scalars(select(BoardColumn).where(BoardColumn.board_id == board_id))
        return list(result.all())