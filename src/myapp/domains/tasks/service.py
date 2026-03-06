from typing import List
from asyncio import Task
from typing import Optional

from myapp.domains.tasks.repositories import TaskRepositoryProtocol
from myapp.domains.tasks.schemas import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, repository: TaskRepositoryProtocol):
        self.repository = repository

    async def create_task(self, column_id: int, new_task: TaskCreate) -> Task:
        return await self.repository.create_task(column_id, new_task)

    async def get_tasks_by_column_id(self, column_id: int) -> List[Task]:
        return await self.repository.get_tasks_by_column_id(column_id)

    async def update_task(self, task_id: int, task_update: TaskUpdate) -> Optional[Task]:
        return await self.repository.update_task(task_id, task_update)

    async def delete_task(self, task_id: int) -> bool:
        return await self.repository.delete_task(task_id)