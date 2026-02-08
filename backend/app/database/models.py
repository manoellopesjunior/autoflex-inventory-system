from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class ProductRawMaterial(Base):
    __tablename__ = "product_raw_materials"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    raw_material_id = Column(Integer, ForeignKey("raw_materials.id"), primary_key=True)
    quantity = Column(Float, nullable=False)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    raw_materials = relationship(
        "ProductRawMaterial",
        backref="product",
        cascade="all, delete-orphan"
    )


class RawMaterial(Base):
    __tablename__ = "raw_materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    stock = Column(Float, nullable=False)

    products = relationship(
        "ProductRawMaterial",
        backref="raw_material",
        cascade="all, delete-orphan"
    )
