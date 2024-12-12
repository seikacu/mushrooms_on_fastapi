from typing import List

from pydantic import BaseModel, ConfigDict, Field


class MushroomAdd(BaseModel):
    name: str = Field(max_length=100, description="Название гриба (до 100 символов)")
    edible: bool = Field(..., description="Указывает, съедобен ли гриб")
    weight: int = Field(
        ge=5, le=1000, description="Вес гриба в граммах (от 5 до 1000 грамм)"
    )
    freshness: bool = Field(..., description="Указывает, свежий ли гриб")

    model_config = ConfigDict(extra="forbid")


class MushroomUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        description="Новое название гриба (если требуется обновление)",
    )
    edible: bool | None = Field(
        default=None,
        description="Указывает, съедобен ли гриб (если требуется обновление)",
    )
    weight: int | None = Field(
        default=None,
        description="Новый вес гриба в граммах (если требуется обновление, от 5 до 1000 грамм)",
    )
    freshness: bool | None = Field(
        default=None,
        description="Указывает, свежий ли гриб (если требуется обновление)",
    )

    model_config = ConfigDict(extra="forbid")


class Mushroom(MushroomAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BasketCreate(BaseModel):
    owner: str = Field(
        max_length=250, description="Имя владельца корзины, до 250 символов"
    )
    capacity: int = Field(
        ge=500,
        le=5000,
        description="Максимальная вместимость корзины в граммах (от 500 до 5000 грамм)",
    )
    mushrooms: List[Mushroom] = []

    model_config = ConfigDict(extra="forbid")


class Basket(BasketCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
