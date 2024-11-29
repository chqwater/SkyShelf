from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from contextlib import asynccontextmanager
import pymysql


router = APIRouter()
# SQLAlchemy setup
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class UserInf(Base):
    __tablename__ = "User_inf"
    user_id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255), unique=True, nullable=False)
    user_password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    # Define reverse relationship for better queries
    selected_categories = relationship("UserSelectedCategories", back_populates="user")


class Journey(Base):
    __tablename__ = "Categories"
    categories_id = Column(Integer, primary_key=True, index=True)
    categories_name = Column(String(255), nullable=False)  # Added length to VARCHAR

    # Define reverse relationship for better queries
    selected_by_users = relationship("UserSelectedCategories", back_populates="journey")


class UserSelectedCategories(Base):
    __tablename__ = "User_selected_categories"
    u_id = Column(Integer, ForeignKey("User_inf.user_id"), primary_key=True, index=True)
    c_id = Column(Integer, ForeignKey("Categories.categories_id"), nullable=False)

    # Define relationships
    journey = relationship("Journey", back_populates="selected_by_users")
    user = relationship("UserInf", back_populates="selected_categories")

# Create tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database with seed data if necessary
@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        # Check if journeys exist, otherwise seed them
        if not db.query(Journey).first():
            db.add_all([
                Journey(categories_id=1, categories_name="Philosophy"),
                Journey(categories_id=2, categories_name="Science"),
                Journey(categories_id=3, categories_name="Art")
            ])
            db.commit()
    finally:
        db.close()
    yield  # App continues running



# Pydantic models for validation
class UpdateJourneyRequest(BaseModel):
    user_id: int
    new_journey: list[int]

# API endpoint to update the journey
@router.post("/api/update-journey")
async def update_journey(request: UpdateJourneyRequest, db: SessionLocal = Depends(get_db)):
    # Check if the user exists
    user = db.query(UserInf).filter(UserInf.user_id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {request.user_id} not found")

    # Validate each journey ID in the request
    for journey_id in request.new_journey:
        journey = db.query(Journey).filter(Journey.categories_id == journey_id).first()
        if not journey:
            raise HTTPException(status_code=404, detail=f"Journey with id {journey_id} not found")

    # Remove all existing selections for this user
    db.query(UserSelectedCategories).filter(UserSelectedCategories.u_id == request.user_id).delete()

    # Insert new selections
    new_selections = [
        UserSelectedCategories(u_id=request.user_id, c_id=journey_id)
        for journey_id in request.new_journey
    ]
    db.bulk_save_objects(new_selections)
    db.commit()

    # Return success response
    return {
        "message": "Journey updated successfully",
        "user_id": request.user_id,
        "new_journey_ids": request.new_journey
    }
