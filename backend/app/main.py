from fastapi import FastAPI

from app.database.database import Base, engine
from app.routers.product import router as product_router
from app.routers.raw_material import router as raw_material_router
from app.routers.product_raw_material import router as product_raw_material_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Autoflex Inventory System")

app.include_router(product_router)
app.include_router(raw_material_router)
app.include_router(product_raw_material_router)


