# app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Ambil URL database dari environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/chatbot")

# Buat engine database
engine = create_engine(DATABASE_URL)

# Buat session untuk mengakses database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk definisi model SQLAlchemy
Base = declarative_base()
