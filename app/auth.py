from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models import User
from app.database import get_db
import jwt

router = APIRouter(prefix="/auth", tags=["auth"])
SECRET_KEY = "smartstake-secret"

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username, User.password == user.password).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"user_id": db_user.id}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}

@router.post("/register")
def register(user: UserLogin, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}