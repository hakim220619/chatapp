# app/core/auth.py

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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    expiration = timedelta(minutes=30)
    expire = datetime.utcnow() + expiration
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    print(f"Generated Token: {encoded_jwt}")
    return encoded_jwt
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            print("Username is missing in the payload")
            raise credentials_exception

    except jwt.PyJWTError as e:
        print(f"Error decoding JWT: {e}")
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        print(f"User with username {username} not found")
        raise credentials_exception

    return user
