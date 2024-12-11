from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database import create_tables, delete_tables
from router import all_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(title="Поход за грибами", lifespan=lifespan)

for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
