from typing import List

from pydantic import BaseModel, ConfigDict


class Mushroom(BaseModel):
    id: int
    name: str
    edible: bool
    weight: int  # в граммах
    freshness: str

    model_config = ConfigDict(from_attributes=True)


class Basket(BaseModel):
    id: int
    owner: str
    capacity: int  # в граммах
    mushrooms: List[Mushroom] = []

    model_config = ConfigDict(from_attributes=True)
