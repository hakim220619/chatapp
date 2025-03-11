from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes import  user, auth

app = FastAPI()

# Migrasi database
Base.metadata.create_all(bind=engine)

# Tambahkan router
app.include_router(auth.router, prefix="/api", tags=["Auth"])
app.include_router(user.router, prefix="/api", tags=["Users"])
