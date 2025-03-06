# app/models/product.py

from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

# Definisi tabel Product menggunakan SQLAlchemy
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
