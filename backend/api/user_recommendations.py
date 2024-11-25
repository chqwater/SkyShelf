from fastapi import FastAPI, HTTPException, Path, Depends, APIRouter
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError
from typing import List

router = APIRouter()
# Database connection details
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    favorite_journey_id = Column(Integer, ForeignKey("journeys.id"))
    favorite_journey = relationship("Journey", back_populates="users")

class Journey(Base):
    __tablename__ = "journeys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    users = relationship("User", back_populates="favorite_journey")
    books = relationship("Book", back_populates="journey")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String, nullable=False)
    file_url = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    journey_id = Column(Integer, ForeignKey("journeys.id"))
    journey = relationship("Journey", back_populates="books")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoint
@router.get("/api/recommendation/{u_id}")
async def get_recommendations(u_id: int = Path(..., title="The ID of the user to get recommendations for"), db: SessionLocal = Depends(get_db)):
    try:
        # Check if user exists
        user = db.query(User).filter(User.id == u_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id {u_id} not found")

        # Fetch favorite journey
        favorite_journey = user.favorite_journey
        if not favorite_journey:
            raise HTTPException(status_code=404, detail="Favorite journey not set for this user")

        # Fetch 10 journeys and their books
        journeys = db.query(Journey).all()
        if len(journeys) == 0:
            raise HTTPException(status_code=404, detail="No journeys found")

        recommendations = []
        for journey in journeys:
            # Get 3 books for each journey
            books = db.query(Book).filter(Book.journey_id == journey.id).limit(3).all()
            if not books:
                continue
            recommendations.append({
                "id": journey.id,
                "name": journey.name,
                "books": [{
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "description": book.description,
                    "file_url": book.file_url,
                    "img_url": book.img_url
                } for book in books]
            })

        # Prioritize favorite journey
        recommendations.sort(key=lambda x: x["id"] != favorite_journey.id)

        # Limit to 10 journeys
        recommendations = recommendations[:10]

        return {"recommendations": recommendations}

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
