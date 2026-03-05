from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from typing import Optional, List, Text
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Board(Base):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    columns: Mapped[List[BoardColumn]] = relationship(cascade="all, delete-orphan", back_populates="board")


class BoardColumn(Base):
    __tablename__ = "columns"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    color: Mapped[Optional[str]]
    position: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))

    board: Mapped[Board] = relationship(back_populates="columns")
    
    tasks: Mapped[List[Task]] = relationship(cascade="all, delete-orphan", back_populates="column")


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[Optional[Text]]
    position: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    column_id: Mapped[int] = mapped_column(ForeignKey("columns.id"))

    column: Mapped[BoardColumn] = relationship(back_populates="tasks")