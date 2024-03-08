from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated
from contextlib import asynccontextmanager

from fast_api.database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")


app = FastAPI(lifespan=lifespan)


class TaskCreate(BaseModel):
    name: str
    description: str | None = None


class TaskRead(TaskCreate):
    id: int


tasks = []


@app.post('/tasks')
async def task_create(
        task: Annotated[TaskCreate, Depends()]
):
    tasks.append(task)
    return {'ok': True}
