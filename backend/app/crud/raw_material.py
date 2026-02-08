from sqlalchemy.orm import Session
from app.database import models
from app.schemas.raw_material import RawMaterialCreate, RawMaterialUpdate


def get_raw_materials(db: Session):
    return db.query(models.RawMaterial).all()


def get_raw_material(db: Session, raw_material_id: int):
    return (
        db.query(models.RawMaterial)
        .filter(models.RawMaterial.id == raw_material_id)
        .first()
    )


def create_raw_material(db: Session, raw_material: RawMaterialCreate):
    db_raw_material = models.RawMaterial(
        name=raw_material.name,
        stock=raw_material.stock
    )
    db.add(db_raw_material)
    db.commit()
    db.refresh(db_raw_material)
    return db_raw_material


def update_raw_material(
    db: Session,
    raw_material_id: int,
    raw_material: RawMaterialUpdate
):
    db_raw_material = get_raw_material(db, raw_material_id)
    if not db_raw_material:
        return None

    if raw_material.name is not None:
        db_raw_material.name = raw_material.name

    if raw_material.stock is not None:
        db_raw_material.stock = raw_material.stock

    db.commit()
    db.refresh(db_raw_material)
    return db_raw_material


def delete_raw_material(db: Session, raw_material_id: int):
    db_raw_material = get_raw_material(db, raw_material_id)
    if not db_raw_material:
        return None

    db.delete(db_raw_material)
    db.commit()
    return db_raw_material
