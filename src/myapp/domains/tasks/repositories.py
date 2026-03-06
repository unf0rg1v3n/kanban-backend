from typing import List, Optional, Protocol
from myapp.db.models import Task
from myapp.domains.tasks.schemas import TaskCreate, TaskUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class TaskRepositoryProtocol(Protocol):
    async def create_task(self, column_id: int, new_task: TaskCreate) -> Task:
        ...
    
    async def get_tasks_by_column_id(self, column_id: int) -> List[Task]:
        ...

    async def update_task(self, task_id: int, task_update: TaskUpdate) -> Optional[Task]:
        ...
    
    async def delete_task(self, task_id: int) -> bool:
        ...


class PostgresTaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_task(self, column_id: int, new_task: TaskCreate) -> Task:
        task = Task(column_id=column_id, title=new_task.title, description=new_task.description,
                    position=new_task.position)
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def get_tasks_by_column_id(self, column_id: int) -> List[Task]:
        result = await self.session.scalars(select(Task).where(Task.column_id == column_id))
        return list(result.all())

    async def update_task(self, task_id: int, task_update: TaskUpdate) -> Optional[Task]:
        task = await self.session.get(Task, task_id)
        if not task:
            return None
        update_dict = task_update.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(task, key, value)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete_task(self, task_id: int) -> bool:
        task = await self.session.get(Task, task_id)
        if not task:
            return False
        await self.session.delete(task)
        await self.session.commit()
        return True