from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class BoardCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class BoardRead(BaseModel):
    id: int
    title: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)