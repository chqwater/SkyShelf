from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import bcrypt
from datetime import datetime, timedelta

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
    role = Column(String(255), nullable=False)


# Pydantic Model for Request Body
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Dependency for DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Verify Password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


# Login User Endpoint
@router.post("/api/login")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # Check if the user exists
    db_user = db.query(UserInf).filter(UserInf.user_email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Verify the user's password
    if not verify_password(user.password, db_user.user_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")


    # Return the token and user info
    return {
        "message": "Login successful",
        "email": db_user.user_email,
        "username": db_user.user_name,
        "role": db_user.role
    }
