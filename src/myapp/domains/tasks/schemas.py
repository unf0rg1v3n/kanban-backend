from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    position: int


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    position: int
    created_at: datetime
    column_id: int

    model_config = ConfigDict(from_attributes=True)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    position: int | None = None
    column_id: int | None = None