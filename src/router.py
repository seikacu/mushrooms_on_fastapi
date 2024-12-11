from typing import Annotated

from fastapi import APIRouter, Depends

from repository import BasketRepository, MushroomRepository
from schemas import Basket, BasketCreate, Mushroom, MushroomAdd, MushroomUpdate

router_mushrooms = APIRouter(
    prefix="/mushrooms",
    tags=["Грибы"],
)

router_baskets = APIRouter(
    prefix="/baskets",
    tags=["Корзинки"],
)


all_routers = [
    router_mushrooms,
    router_baskets,
]


# Эндпоинты для работы с грибами
@router_mushrooms.post("/add")
async def add_mushroom(mushroom: Annotated[MushroomAdd, Depends()]) -> Mushroom:
    mushroom_db = await MushroomRepository.add_one(mushroom)
    return mushroom_db


@router_mushrooms.put("/update/{mushroom_id}")
async def update_mushroom(
    mushroom_id: int, mushroom: Annotated[MushroomUpdate, Depends()]
) -> Mushroom:
    mushroom_db = await MushroomRepository.update_one(mushroom_id, mushroom)
    return mushroom_db


@router_mushrooms.get("/get/{mushroom_id}")
async def get_mushroom(mushroom_id: int) -> Mushroom:
    mushroom_db = await MushroomRepository.get_one(mushroom_id)
    return mushroom_db


# Эндпоинты для работы с корзинками
@router_baskets.post("/create")
async def create_basket(basket: Annotated[BasketCreate, Depends()]) -> Basket:
    basket_db = await BasketRepository.create_one(basket)
    return basket_db


@router_baskets.post("/{basket_id}/mushrooms/")
async def put_mushroom_to_basket(basket_id: int, mushroom_id: int) -> Basket:
    db_basket = await BasketRepository.put_mushroom(basket_id, mushroom_id)
    return db_basket


@router_baskets.delete("/{basket_id}/mushrooms/{mushroom_id}")
async def remove_mushroom_from_basket(basket_id: int, mushroom_id: int) -> Basket:
    db_basket = await BasketRepository.del_mushroom(basket_id, mushroom_id)
    return db_basket


@router_baskets.get("/{basket_id}")
async def get_basket(basket_id: int):
    db_basket = await BasketRepository.get_mushrooms(basket_id)
    return db_basket
