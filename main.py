from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import create_tables, delete_tables
from src.router import all_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(
    title="Поход за грибами",
    lifespan=lifespan,
    description="API, чтобы сходить по грибы)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

for router in all_routers:
    app.include_router(router)
