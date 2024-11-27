# app/main.py
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, create_engine, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import bcrypt

router = APIRouter()

# Database Configuration
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model
class UserInf(Base):
    __tablename__ = "User_inf"
    user_id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255), unique=True, nullable=False)
    user_password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Model for Request Body
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    username: str

# Dependency for DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Hash Password
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Register User Endpoint
@router.post("/api/register")
async def register_user(user: UserRegister, db: Session = Depends(get_db)):
    # Check if the email is already registered
    existing_user = db.query(UserInf).filter(UserInf.user_email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered")

    # Hash the user's password
    hashed_password = hash_password(user.password)

    # Create a new user
    new_user = UserInf(user_email=user.email, user_password=hashed_password, user_name=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.user_id, "username": new_user.user_name, "email": new_user.user_email}
