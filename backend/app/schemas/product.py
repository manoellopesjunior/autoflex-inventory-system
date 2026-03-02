from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    price: float | None = Field(default=None, gt=0)


class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True

