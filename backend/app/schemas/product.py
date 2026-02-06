from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    quantity: int | None = None

class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True  # <- importante para Pydantic v2


