from fastapi import FastAPI
from app.database.database import engine
from app.database import models
from app.routers import products

# Cria todas as tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Autoflex Inventory API", version="0.1.0")

# Incluindo router de produtos
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "API is running"}

