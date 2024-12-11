from typing import List

from pydantic import BaseModel, ConfigDict


class MushroomAdd(BaseModel):
    name: str
    edible: bool
    weight: int  # в граммах
    freshness: str


class Mushroom(MushroomAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Basket(BaseModel):
    id: int
    owner: str
    capacity: int  # в граммах
    mushrooms: List[Mushroom] = []

    model_config = ConfigDict(from_attributes=True)
