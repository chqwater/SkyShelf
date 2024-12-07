from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
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
    role = Column(String(255), nullable=False)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Model for Request Body
class UpdatePasswordRequest(BaseModel):
    user_id: int
    new_password: str

# Hash Password
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# API Endpoint to Update Password
@router.post("/api/new_password")
async def update_password(request: UpdatePasswordRequest, db: Session = Depends(get_db)):
    # Input validation
    if not request.user_id or not request.new_password:
        raise HTTPException(status_code=400, detail="Both user_id and new_password are required")

    # Check if the user exists in the User table
    user = db.query(UserInf).filter(UserInf.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {request.user_id} not found")

    # Hash the new password
    hashed_password = hash_password(request.new_password)

    # Update the user's password
    user.password = hashed_password
    db.commit()

    # If the user is an admin, update the password in the Admin table as well
    if user.is_admin:
        admin = db.query(UserInf).filter(UserInf.user_id == user.id).first()
        if admin:
            admin.password = hashed_password
            db.commit()

    # Return success response
    return {"user_id": request.user_id}
