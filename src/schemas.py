from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class MushroomAdd(BaseModel):
    name: str
    edible: bool
    weight: int  # в граммах
    freshness: bool


class MushroomUpdate(BaseModel):
    name: Optional[str] = None
    edible: Optional[bool] = None
    weight: Optional[int] = None  # в граммах
    freshness: Optional[bool] = None


class Mushroom(MushroomAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BasketCreate(BaseModel):
    owner: str
    capacity: int  # в граммах
    mushrooms: List[Mushroom] = []


class Basket(BasketCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
