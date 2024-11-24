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
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    journey_id = Column(Integer, ForeignKey("journeys.id"), nullable=True)
    journey = relationship("Journey")

class Journey(Base):
    __tablename__ = "journeys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)  # Added length to VARCHAR

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
                Journey(id=1, name="Philosophy"),
                Journey(id=2, name="Science"),
                Journey(id=3, name="Art")
            ])
            db.commit()
    finally:
        db.close()
    yield  # App continues running


# Pydantic models for validation
class UpdateJourneyRequest(BaseModel):
    user_id: int
    journey: int

# API endpoint to update the journey
@router.post("/api/update-journey")
async def update_journey(request: UpdateJourneyRequest, db: SessionLocal = Depends(get_db)):
    # Check if the user exists
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {request.user_id} not found")

    # Check if the journey exists
    journey = db.query(Journey).filter(Journey.id == request.journey).first()
    if not journey:
        raise HTTPException(status_code=404, detail=f"Journey with id {request.journey} not found")

    # Update user's journey
    user.journey_id = journey.id
    db.commit()

    # Return success response
    return {
        "message": "Journey updated successfully",
        "user_id": user.id,
        "new_journey": journey.name,
        "new_journey_id": journey.id
    }

