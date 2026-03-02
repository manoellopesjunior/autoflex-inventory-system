from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database.models import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, product: ProductCreate):
    try:
        db_product = Product(
            name=product.name,
            price=product.price
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao criar produto")


def get_products(db: Session):
    try:
        return db.query(Product).all()
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar produtos")


def get_product_by_id(db: Session, product_id: int):
    try:
        return db.query(Product).filter(Product.id == product_id).first()
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao buscar produto")


def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None

    try:
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)

        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao atualizar produto")


def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None

    try:
        db.delete(db_product)
        db.commit()
        return db_product
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao deletar produto")