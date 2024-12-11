from fastapi import HTTPException
from sqlalchemy import select

from src.database import BasketModel, MushroomModel, async_session_factory
from src.schemas import BasketCreate, MushroomAdd, MushroomUpdate


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

    @classmethod
    async def update_one(cls, mushroom_id: int, data: MushroomUpdate):
        async with async_session_factory() as session:
            async with session.begin():
                result = await session.execute(
                    select(MushroomModel).filter(MushroomModel.id == mushroom_id)
                )
                db_mushroom = result.scalars().first()
                if db_mushroom is None:
                    raise HTTPException(status_code=404, detail="Mushroom not found.")
                for key, value in data.dict(exclude_unset=True).items():
                    if value is not None:
                        setattr(db_mushroom, key, value)
                await session.commit()
                return db_mushroom

    @classmethod
    async def get_one(cls, mushroom_id: int):
        async with async_session_factory() as session:
            async with session.begin():
                result = await session.execute(
                    select(MushroomModel).filter(MushroomModel.id == mushroom_id)
                )
                db_mushroom = result.scalars().first()
                if db_mushroom is None:
                    raise HTTPException(status_code=404, detail="Mushroom not found.")
                return db_mushroom


class BasketRepository:
    @classmethod
    async def create_one(cls, data: BasketCreate):
        async with async_session_factory() as session:
            basket_dict = data.model_dump()
            basket = BasketModel(**basket_dict)
            session.add(basket)
            await session.flush()
            await session.commit()
            return basket

    @classmethod
    async def put_mushroom(cls, basket_id: int, mushroom_id: int):
        async with async_session_factory() as session:
            async with session.begin():
                result_basket = await session.execute(
                    select(BasketModel).filter(BasketModel.id == basket_id)
                )
                db_basket = result_basket.scalars().first()

                result_mushroom = await session.execute(
                    select(MushroomModel).filter(MushroomModel.id == mushroom_id)
                )
                db_mushroom = result_mushroom.scalars().first()

                if db_basket is None:
                    raise HTTPException(status_code=404, detail="Basket not found.")
                if db_mushroom is None:
                    raise HTTPException(status_code=404, detail="Mushroom not found.")

                # Проверка вместимости корзинки
                current_weight = sum(m.weight for m in db_basket.mushrooms)
                if current_weight + db_mushroom.weight > db_basket.capacity:
                    raise HTTPException(
                        status_code=400, detail="Not enough capacity in the basket."
                    )

                # Добавление гриба в корзинку
                db_basket.mushrooms.append(db_mushroom)
                await session.commit()
                return db_basket

    @classmethod
    async def del_mushroom(cls, basket_id: int, mushroom_id: int):
        async with async_session_factory() as session:
            async with session.begin():
                result_basket = await session.execute(
                    select(BasketModel).filter(BasketModel.id == basket_id)
                )
                db_basket = result_basket.scalars().first()

                if db_basket is None:
                    raise HTTPException(status_code=404, detail="Basket not found.")

                # Поиск гриба в корзинке
                mushroom = next(
                    (m for m in db_basket.mushrooms if m.id == mushroom_id), None
                )

                if mushroom is None:
                    raise HTTPException(
                        status_code=404, detail="Mushroom not found in the basket."
                    )

                # Удаление гриба из корзинки
                db_basket.mushrooms.remove(mushroom)
                await session.commit()
                return db_basket

    @classmethod
    async def get_mushrooms(cls, basket_id: int):
        async with async_session_factory() as session:
            async with session.begin():
                result_basket = await session.execute(
                    select(BasketModel).filter(BasketModel.id == basket_id)
                )
                db_basket = result_basket.scalars().first()

                if db_basket is None:
                    raise HTTPException(status_code=404, detail="Basket not found.")

                # result_mushrooms = await session.execute(
                #     select(MushroomModel).filter(
                #         MushroomModel.id.in_(
                #             [mushroom.id for mushroom in db_basket.mushrooms]
                #         )
                #     )
                # )
                # db_mushrooms = result_mushrooms.scalars().all()

                return db_basket
