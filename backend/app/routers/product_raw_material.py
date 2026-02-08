from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.product_raw_material import (
    ProductRawMaterialCreate,
    ProductRawMaterialOut,
)
from app.crud import product_raw_material as crud_prm

router = APIRouter(
    prefix="/product-raw-materials",
    tags=["Product Raw Materials"]
)


@router.post("/", response_model=ProductRawMaterialOut, status_code=201)
def add_raw_material_to_product(
    data: ProductRawMaterialCreate,
    db: Session = Depends(get_db)
):
    result, error = crud_prm.add_raw_material_to_product(db, data)

    if error == "product_not_found":
        raise HTTPException(status_code=404, detail="Product not found")

    if error == "raw_material_not_found":
        raise HTTPException(status_code=404, detail="Raw material not found")

    return result


@router.get(
    "/product/{product_id}",
    response_model=list[ProductRawMaterialOut]
)
def get_raw_materials_by_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return crud_prm.get_raw_materials_by_product(db, product_id)


@router.delete(
    "/product/{product_id}/raw-material/{raw_material_id}",
    response_model=ProductRawMaterialOut
)
def delete_raw_material_from_product(
    product_id: int,
    raw_material_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud_prm.delete_raw_material_from_product(
        db, product_id, raw_material_id
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Relation not found")

    return deleted
