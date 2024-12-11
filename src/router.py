from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from src.database import MushroomModel
from src.repository import MushroomRepository
from src.schemas import Mushroom, MushroomAdd

router_mushrooms = APIRouter(
    prefix="/mushrooms",
    tags=["Грибы"],
)

all_routers = [
    router_mushrooms,
]


# Эндпоинты для работы с грибами
@router_mushrooms.post("")
async def add_mushroom(mushroom: Annotated[MushroomAdd, Depends()]) -> Mushroom:
    mushroom_db = await MushroomRepository.add_one(mushroom)
    return mushroom_db


# @router_mushrooms.put("/mushrooms/{mushroom_id}", response_model=Mushroom)
# def update_mushroom(
#     mushroom_id: int, mushroom: Mushroom, db: SessionLocal = Depends(get_db)
# ):
#     db_mushroom = (
#         db.query(MushroomModel).filter(MushroomModel.id == mushroom_id).first()
#     )
#     if db_mushroom is None:
#         raise HTTPException(status_code=404, detail="Mushroom not found.")
#     for key, value in mushroom.dict().items():
#         setattr(db_mushroom, key, value)
#     db.commit()
#     return Mushroom.from_orm(db_mushroom)


# @router_mushrooms.get("/mushrooms/{mushroom_id}", response_model=Mushroom)
# def get_mushroom(mushroom_id: int, db: SessionLocal = Depends(get_db)):
#     db_mushroom = (
#         db.query(MushroomModel).filter(MushroomModel.id == mushroom_id).first()
#     )
#     if db_mushroom is None:
#         raise HTTPException(status_code=404, detail="Mushroom not found.")
#     return Mushroom.from_orm(db_mushroom)


# # Эндпоинты для работы с корзинками
# @router.post("/baskets/", response_model=Basket)
# def create_basket(basket: Basket, db: SessionLocal = Depends(get_db)):
#     db_basket = BasketModel(**basket.dict())
#     db.add(db_basket)
#     db.commit()
#     db.refresh(db_basket)
#     return Basket.from_orm(db_basket)


# @router.post("/baskets/{basket_id}/mushrooms/", response_model=Basket)
# def add_mushroom_to_basket(
#     basket_id: int, mushroom_id: int, db: SessionLocal = Depends(get_db)
# ):
#     db_basket = db.query(BasketModel).filter(BasketModel.id == basket_id).first()
#     db_mushroom = (
#         db.query(MushroomModel).filter(MushroomModel.id == mushroom_id).first()
#     )

#     if db_basket is None:
#         raise HTTPException(status_code=404, detail="Basket not found.")
#     if db_mushroom is None:
#         raise HTTPException(status_code=404, detail="Mushroom not found.")

#     # Проверка вместимости корзинки
#     current_weight = sum(m.weight for m in db_basket.mushrooms)
#     if current_weight + db_mushroom.weight > db_basket.capacity:
#         raise HTTPException(
#             status_code=400, detail="Not enough capacity in the basket."
#         )

#     # Добавление гриба в корзинку
#     db_basket.mushrooms.append(db_mushroom)
#     db.commit()
#     return Basket.from_orm(db_basket)


# @router.delete("/baskets/{basket_id}/mushrooms/{mushroom_id}", response_model=Basket)
# def remove_mushroom_from_basket(
#     basket_id: int, mushroom_id: int, db: SessionLocal = Depends(get_db)
# ):
#     db_basket = db.query(BasketModel).filter(BasketModel.id == basket_id).first()

#     if db_basket is None:
#         raise HTTPException(status_code=404, detail="Basket not found.")

#     # Поиск гриба в корзинке
#     mushroom_to_remove = next(
#         (m for m in db_basket.mushrooms if m.id == mushroom_id), None
#     )

#     if mushroom_to_remove is None:
#         raise HTTPException(status_code=404, detail="Mushroom not found in the basket.")

#     # Удаление гриба из корзинки
#     db_basket.mushrooms.remove(mushroom_to_remove)
#     db.commit()
#     return Basket.from_orm(db_basket)


# @router.get("/baskets/{basket_id}", response_model=Basket)
# def get_basket(basket_id: int, db: SessionLocal = Depends(get_db)):
#     db_basket = db.query(BasketModel).filter(BasketModel.id == basket_id).first()
#     if db_basket is None:
#         raise HTTPException(status_code=404, detail="Basket not found.")

#     # Получение грибов из корзинки
#     mushrooms = (
#         db.query(MushroomModel)
#         .filter(MushroomModel.id.in_([mushroom.id for mushroom in db_basket.mushrooms]))
#         .all()
#     )

#     # Создание Pydantic модели корзинки с грибами
#     return Basket.from_orm(db_basket)
