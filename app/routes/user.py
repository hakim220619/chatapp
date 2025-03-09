from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.models.user import User
from app.core.database import SessionLocal
from app.core.auth import get_password_hash, get_current_user
from app.utils.custome_respond import response

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", tags=["Users"])
def get_all_users(token: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Endpoint untuk mendapatkan daftar semua pengguna dari database. Harus terautentikasi.
    """
    data = db.query(User).all()
    if not data:
        raise HTTPException(status_code=404, detail="No users found")
    return response(200, "Users", "GET", data)



@router.post("/users", tags=["Users"])
def create_user(params: UserCreate, db: Session = Depends(get_db), token: User = Depends(get_current_user)):
    """
    Endpoint untuk membuat pengguna baru.
    """
    existing_user = db.query(User).filter((User.username == params.username) | (User.email == params.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = get_password_hash(params.password)
    new_data = User(
        username=params.username,
        email=params.email,
        password=hashed_password,
        role_id=params.role_id
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return response(201, "Users", "POST")

@router.get("/users/{ref_id}", tags=["Users"])
def get_user_by_id(ref_id: int, db: Session = Depends(get_db), token: User = Depends(get_current_user)):
    """
    Endpoint untuk mendapatkan pengguna berdasarkan ID.
    """
    data = db.query(User).filter(User.id == ref_id).first()
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    return response(200, "Users", "GET", data)


@router.get("/users", response_model=list[UserResponse], tags=["Users"])
def get_all_users(db: Session = Depends(get_db), token: User = Depends(get_current_user)):
    """
    Endpoint untuk mendapatkan semua pengguna.
    """
    data = db.query(User).all()
    return response(200, "Users", "GET", data)


@router.put("/users/{ref_id}", tags=["Users"])
def update_user(ref_id: int, user_update: UserUpdate, db: Session = Depends(get_db), token: User = Depends(get_current_user)):
    """
    Endpoint untuk memperbarui pengguna.
    """
    user = db.query(User).filter(User.id == ref_id).first()
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

@router.delete("/users/{ref_id}", tags=["Users"])
def delete_user(ref_id: int, db: Session = Depends(get_db), token: User = Depends(get_current_user)):
    """
    Endpoint untuk menghapus pengguna.
    """
    data = db.query(User).filter(User.id == ref_id).first()
    if not data:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(data)
    db.commit()
    return response(200, "User", "DELETE")
