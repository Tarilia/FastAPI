from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()


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
