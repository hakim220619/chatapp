from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import product, user

app = FastAPI()

# Migrasi database
Base.metadata.create_all(bind=engine)

# Tambahkan router
app.include_router(product.router, prefix="/api", tags=["Products"])
app.include_router(user.router, prefix="/api", tags=["Users"])
