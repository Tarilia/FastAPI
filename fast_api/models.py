from pydantic import BaseModel


class TaskCreate(BaseModel):
    name: str
    description: str | None = None


class TaskRead(TaskCreate):
    id: int
