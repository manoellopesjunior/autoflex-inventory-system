from pydantic import BaseModel
from typing import List, Optional

class RawMaterialOut(BaseModel):
    id: int
    name: str
    stock: float

    class Config:
        from_attributes = True

class ProductRawMaterialOut(BaseModel):
    raw_material: RawMaterialOut
    quantity: float

    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

class ProductOut(ProductBase):
    id: int
    raw_materials: List[ProductRawMaterialOut] = []

    class Config:
        from_attributes = True
