from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
    role_id = Column(Integer)  # Add role_id as an Integer field
    google_id = Column(String, unique=True, index=True)  # Add google_id as a unique String
    account_status = Column(String, default="active")  # Add account_status, default to "active"
