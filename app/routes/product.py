# app/routes/product.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.product import Product
from app.core.database import SessionLocal

router = APIRouter()

# Dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products", tags=["Products"])
def get_all_products(db: Session = Depends(get_db)):
    """
    Endpoint untuk mendapatkan daftar semua produk dari database.
    """
    products = db.query(Product).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products
