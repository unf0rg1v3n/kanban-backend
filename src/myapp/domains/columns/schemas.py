from pydantic import BaseModel, Field, ConfigDict

class ColumnCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    position: int
    color: str | None = None


class ColumnRead(BaseModel):
    id: int
    title: str
    position: int
    color: str | None = None
    board_id: int

    model_config = ConfigDict(from_attributes=True)


class ColumnUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    position: int | None = None
    color: str | None = None
