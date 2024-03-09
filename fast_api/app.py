from fastapi import FastAPI
from contextlib import asynccontextmanager

from fast_api.database import create_tables, delete_tables
from fast_api.router import router  as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
