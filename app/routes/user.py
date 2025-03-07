from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.models.user import User
from app.core.database import SessionLocal
from app.core.auth import get_password_hash
from app.utils.custome_respond import response

router = APIRouter()

# Dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", tags=["Users"])
def get_all_users(db: Session = Depends(get_db)):
    """
    Endpoint untuk mendapatkan daftar semua pengguna dari database.
    """
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return response(200, "Users", "GET", users)

@router.post("/users", response_model=UserResponse, tags=["Users"])
def create_user(params: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint untuk membuat pengguna baru.
    """
    existing_user = db.query(User).filter((User.username == params.username) | (User.email == params.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = get_password_hash(params.password)
    new_user = User(
        username=params.username,
        email=params.email,
        password=hashed_password,
        role_id=params.role_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return response(201, "Users", "POST")

@router.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint untuk mendapatkan pengguna berdasarkan ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", response_model=list[UserResponse], tags=["Users"])
def get_all_users(db: Session = Depends(get_db)):
    """
    Endpoint untuk mendapatkan semua pengguna.
    """
    users = db.query(User).all()
    return response(200, "Users", "GET", users)


@router.put("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """
    Endpoint untuk memperbarui pengguna.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_update.username:
        user.username = user_update.username
    if user_update.email:
        user.email = user_update.email
    if user_update.password:
        user.hashed_password = get_password_hash(user_update.password)

    db.commit()
    db.refresh(user)
    return response(200, "User", "PUT", user)

@router.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint untuk menghapus pengguna.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return response(200, "User", "DELETE")
