from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String, create_engine, Enum
from pydantic import BaseModel
from enum import Enum as PyEnum

router = APIRouter()

class RoleEnum(str, PyEnum):
    user = "user"
    admin = "admin"

# Database Configuration
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class EditUserInfoRequest(BaseModel):
    user_id: int
    user_name: str = None
    role: RoleEnum = None

class UserInf(Base):
    __tablename__ = "User_inf"
    user_id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255), nullable=False, unique=True)
    user_name = Column(String(255), nullable=False)
    user_password = Column(String(255), nullable=False)
    role = Column(Enum("user", "admin"), nullable=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/admin/edit-user-info")
async def edit_user_info(request: EditUserInfoRequest, db: Session = Depends(get_db)):
    try:
        user = db.query(UserInf).filter(UserInf.user_id == request.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id {request.user_id} not found")

        if request.user_name is not None:
            user.user_name = request.user_name
        if request.role is not None:
            user.role = request.role

        db.commit()

        return {
            "message": "User information updated successfully",
            "user_id": user.user_id,
            "user_name": user.user_name,
            "role": user.role,
        }

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")