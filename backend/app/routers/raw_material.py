from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.raw_material import (
    RawMaterial,
    RawMaterialCreate,
    RawMaterialUpdate,
)
from app.crud import raw_material as crud_raw_material

router = APIRouter(
    prefix="/raw-materials",
    tags=["Raw Materials"]
)


@router.get("/", response_model=list[RawMaterial])
def read_raw_materials(db: Session = Depends(get_db)):
    return crud_raw_material.get_raw_materials(db)


@router.get("/{raw_material_id}", response_model=RawMaterial)
def read_raw_material(raw_material_id: int, db: Session = Depends(get_db)):
    raw_material = crud_raw_material.get_raw_material(db, raw_material_id)
    if not raw_material:
        raise HTTPException(status_code=404, detail="Raw material not found")
    return raw_material


@router.post("/", response_model=RawMaterial, status_code=201)
def create_raw_material(
    raw_material: RawMaterialCreate,
    db: Session = Depends(get_db)
):
    return crud_raw_material.create_raw_material(db, raw_material)


@router.put("/{raw_material_id}", response_model=RawMaterial)
def update_raw_material(
    raw_material_id: int,
    raw_material: RawMaterialUpdate,
    db: Session = Depends(get_db)
):
    updated = crud_raw_material.update_raw_material(
        db, raw_material_id, raw_material
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Raw material not found")
    return updated


@router.delete("/{raw_material_id}", response_model=RawMaterial)
def delete_raw_material(raw_material_id: int, db: Session = Depends(get_db)):
    deleted = crud_raw_material.delete_raw_material(db, raw_material_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Raw material not found")
    return deleted
