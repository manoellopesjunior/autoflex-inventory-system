from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.routers.product import router as product_router
from app.routers.raw_material import router as raw_material_router
from app.routers.product_raw_material import router as product_raw_material_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Autoflex Inventory System")

# 🔥 ADICIONE ISSO
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # liberado total só para teste
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
app.include_router(raw_material_router)
app.include_router(product_raw_material_router)


