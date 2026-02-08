from pydantic import BaseModel

class ProductRawMaterialBase(BaseModel):
    product_id: int
    raw_material_id: int
    quantity: float


class ProductRawMaterialCreate(ProductRawMaterialBase):
    pass


class ProductRawMaterialOut(ProductRawMaterialBase):
    class Config:
        from_attributes = True
