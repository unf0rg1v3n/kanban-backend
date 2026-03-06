from myapp.db.core import SessionDep
from myapp.domains.tasks.repositories import PostgresTaskRepository
from myapp.domains.tasks.service import TaskService
from .schemas import TaskCreate, TaskRead, TaskUpdate
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(tags=["tasks"])

def get_tasks_service(session: SessionDep) -> TaskService:
    return TaskService(PostgresTaskRepository(session))


@router.post("/columns/{column_id}/tasks",
             summary="Create a new task", response_model=TaskRead)
async def create_task(board_id: int, column_id: int, task_create: TaskCreate,
                      service: TaskService = Depends(get_tasks_service)):
    return await service.create_task(column_id, task_create)


@router.get("/columns/{column_id}/tasks", summary="Get tasks by column ID", 
            response_model=list[TaskRead])
async def get_tasks(column_id: int, 
                    service: TaskService = Depends(get_tasks_service)):
    task = await service.get_tasks_by_column_id(column_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return task


@router.patch("/tasks/{task_id}", summary="Update a task", response_model=TaskRead)
async def update_task(task_id: int, task_update: TaskUpdate,
                      service: TaskService = Depends(get_tasks_service)):
    updated_task = await service.update_task(task_id, task_update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/tasks/{task_id}", summary="Delete a task", status_code=204)
async def delete_task(task_id: int, service: TaskService = Depends(get_tasks_service)):
    success = await service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}