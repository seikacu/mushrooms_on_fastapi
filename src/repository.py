from sqlalchemy import select

from src.database import MushroomModel, async_session_factory
from src.schemas import Mushroom, MushroomAdd


class MushroomRepository:
    @classmethod
    async def add_one(cls, data: MushroomAdd):
        async with async_session_factory() as session:
            mushroom_dict = data.model_dump()
            mushroom = MushroomModel(**mushroom_dict)
            session.add(mushroom)
            await session.flush()
            await session.commit()
            return mushroom
