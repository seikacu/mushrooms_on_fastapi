from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from typing import Optional

from config import settings

engine = create_async_engine(settings.DATABASE_URL)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


# Модели базы данных
class MushroomModel(Model):
    __tablename__ = "mushrooms"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[Optional[str]] = mapped_column(index=True)
    edible: Mapped[bool] = mapped_column(nullable=False, default=False)
    weight: Mapped[int]  # в граммах
    freshness: Mapped[bool] = mapped_column(nullable=False, default=False)


class BasketModel(Model):
    __tablename__ = "baskets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    owner: Mapped[Optional[str]]
    capacity: Mapped[int]  # в граммах
    mushrooms = relationship("MushroomModel", secondary="basket_mushroom")


class BasketMushroom(Model):
    __tablename__ = "basket_mushroom"
    basket_id: Mapped[int] = mapped_column(ForeignKey("baskets.id"), primary_key=True)
    mushroom_id: Mapped[int] = mapped_column(ForeignKey("mushrooms.id"), primary_key=True)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)