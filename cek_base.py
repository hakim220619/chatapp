
import jwt  # Make sure this is imported correctly
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Optional
from app.core import config
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
import logging

# Coba decode manual untuk melihat jika padding atau formatnya bermasalah
encoded = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkYW5pIiwiZXhwIjoxNzQxNTA2OTk0fQ.Iyss0iLD3Z5fzxYmIHAJlwDuVtNJdn4UK8QZ6DkjiD8"
try:
    decoded = jwt.decode(encoded, config.SECRET_KEY, algorithms=[config.ALGORITHM])
    print(decoded)
except Exception as e:
    print(f"Error while decoding token: {e}")
