from fastapi import APIRouter, Depends
from typing import List
from myapp.db.core import SessionDep
from myapp.domains.columns.repositories import PostgresColumnRepository
from myapp.domains.columns.service import ColumnService
from myapp.domains.columns.schemas import ColumnCreate, ColumnRead


def get_column_service(session: SessionDep) -> ColumnService:
    return ColumnService(PostgresColumnRepository(session))

router = APIRouter(prefix="/boards/{board_id}/columns", tags=["columns"])


@router.post("/", summary="Create a new column", response_model=ColumnRead)
async def create_column(board_id: int, column_create: ColumnCreate, 
                        service: ColumnService = Depends(get_column_service)):
    return await service.create_column(board_id, column_create)


@router.get("/", summary="Get all columns for a board", response_model=List[ColumnRead])
async def get_columns(board_id: int, service: ColumnService = Depends(get_column_service)):
    return await service.get_columns(board_id)