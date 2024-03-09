from fastapi import Depends, APIRouter
from typing import Annotated

from fast_api.repository import TaskRepository
from fast_api.models import TaskCreate


router = APIRouter(
   prefix="/tasks",
   tags=["Таски"])


@router.post('')
async def task_create(
        task: Annotated[TaskCreate, Depends()]):
    task_id = await TaskRepository.add_task(task)
    return {'ok': True, "id": task_id}


@router.get('')
async def show_tasks():
    tasks = await TaskRepository.get_tasks()
    return {'tasks': tasks}
