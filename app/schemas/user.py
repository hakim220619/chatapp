from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role_id: int

class UserCreate(UserBase):
    password: str
    role_id: int

class UserResponse(UserBase):
    id: int
    username: str
    email: str
    role_id: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    role_id: Optional[int]

    class Config:
        orm_mode = True
