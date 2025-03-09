from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv  # Import dotenv

# Muat variabel lingkungan dari file .env
load_dotenv()

# Ambil URL database dari environment variable (tanpa fallback default)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables")

# Buat engine database
engine = create_engine(DATABASE_URL)

# Buat session untuk mengakses database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk definisi model SQLAlchemy
Base = declarative_base()
