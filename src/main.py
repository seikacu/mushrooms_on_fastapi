import os
import sys

from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
# from router import

sys.path.insert(1, os.path.join(sys.path[0], ".."))


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
# app.include_router()
