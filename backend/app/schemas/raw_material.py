from pydantic import BaseModel
from typing import Optional


class RawMaterialBase(BaseModel):
    name: str
    stock: float


class RawMaterialCreate(RawMaterialBase):
    pass


class RawMaterialUpdate(BaseModel):
    name: Optional[str] = None
    stock: Optional[float] = None


class RawMaterial(RawMaterialBase):
    id: int

    class Config:
        from_attributes = True
