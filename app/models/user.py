from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role_id = Column(Integer, default=None) 
    google_id = Column(String, unique=True, index=True, default=None)
    account_status = Column(Boolean, default=True)
