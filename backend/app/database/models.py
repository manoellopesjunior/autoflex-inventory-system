from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    raw_materials = relationship(
        "ProductRawMaterial",
        back_populates="product",
        cascade="all, delete"
    )

class RawMaterial(Base):
    __tablename__ = "raw_materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    products = relationship(
        "ProductRawMaterial",
        back_populates="raw_material",
        cascade="all, delete"
    )

class ProductRawMaterial(Base):
    __tablename__ = "product_raw_materials"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    raw_material_id = Column(Integer, ForeignKey("raw_materials.id"))
    required_quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="raw_materials")
    raw_material = relationship("RawMaterial", back_populates="products")
