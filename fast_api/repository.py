from sqlalchemy import select

from fast_api.database import Task, new_session
from fast_api.models import TaskCreate, TaskRead

class TaskRepository:
   @classmethod
   async def add_task(cls, task: TaskCreate):
       async with new_session() as session:
           data = task.model_dump()
           new_task = Task(**data)
           session.add(new_task)
           await session.flush()
           await session.commit()
           return new_task.id

   @classmethod
   async def get_tasks(cls):
       async with new_session() as session:
           query = select(Task)
           result = await session.execute(query)
           task_models = result.scalars().all()
           return task_models
