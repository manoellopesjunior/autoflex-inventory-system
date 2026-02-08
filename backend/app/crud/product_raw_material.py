from sqlalchemy.orm import Session

from app.database.models import (
    Product,
    RawMaterial,
    ProductRawMaterial
)
from app.schemas.product_raw_material import ProductRawMaterialCreate


def add_raw_material_to_product(
    db: Session,
    data: ProductRawMaterialCreate
):
    # verifica se o produto existe
    product = db.query(Product).filter(Product.id == data.product_id).first()
    if not product:
        return None, "product_not_found"

    # verifica se a matéria-prima existe
    raw_material = (
        db.query(RawMaterial)
        .filter(RawMaterial.id == data.raw_material_id)
        .first()
    )
    if not raw_material:
        return None, "raw_material_not_found"

    # verifica se já existe vínculo produto x matéria-prima
    relation = (
        db.query(ProductRawMaterial)
        .filter(
            ProductRawMaterial.product_id == data.product_id,
            ProductRawMaterial.raw_material_id == data.raw_material_id
        )
        .first()
    )

    # se existir, atualiza a quantidade
    if relation:
        relation.quantity = data.quantity
    else:
        # se não existir, cria o vínculo
        relation = ProductRawMaterial(
            product_id=data.product_id,
            raw_material_id=data.raw_material_id,
            quantity=data.quantity
        )
        db.add(relation)

    db.commit()
    db.refresh(relation)

    return relation, None


def get_raw_materials_by_product(db: Session, product_id: int):
    return (
        db.query(ProductRawMaterial)
        .filter(ProductRawMaterial.product_id == product_id)
        .all()
    )


def delete_raw_material_from_product(
    db: Session,
    product_id: int,
    raw_material_id: int
):
    relation = (
        db.query(ProductRawMaterial)
        .filter(
            ProductRawMaterial.product_id == product_id,
            ProductRawMaterial.raw_material_id == raw_material_id
        )
        .first()
    )

    if not relation:
        return None

    db.delete(relation)
    db.commit()
    return relation

