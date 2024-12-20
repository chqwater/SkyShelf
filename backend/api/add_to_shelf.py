from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, create_engine, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base


router = APIRouter()
# Initialize FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database models
class User(Base):
    __tablename__ = "User_inf"
    user_id = Column(Integer, primary_key=True, index=True)

class Book(Base):
    __tablename__ = "Book"
    book_id = Column(Integer, primary_key=True, index=True)

class UserBook(Base):
    __tablename__ = "User_book"
    user_book_id = Column(Integer, primary_key=True, index=True)
    user_book_u_id = Column(Integer, ForeignKey("User_inf.user_id"), nullable=False)
    user_book_b_id = Column(Integer, ForeignKey("Book.book_id"), nullable=False)
    last_read_time = Column(DateTime, nullable=True, default=datetime.utcnow)
    last_read_position = Column(Integer, nullable=True, default=1)


# Request body model
class AddBookRequest(BaseModel):
    user_id: int = Field(..., description="The ID of the user")
    book_id: int = Field(..., description="The ID of the book")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/add_book")
async def add_book_to_current_reading(data: AddBookRequest, db: SessionLocal = Depends(get_db)):
    # Input validation is already handled by Pydantic

    # Check if the user exists
    user = db.query(User).filter_by(user_id=data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the book exists
    book = db.query(Book).filter_by(book_id=data.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Check if the relationship already exists in UserBook
    existing_relation = db.query(UserBook).filter_by(user_book_u_id=data.user_id, user_book_b_id=data.book_id).first()
    if existing_relation:
        raise HTTPException(status_code=400, detail="The book is already added to the current reading list")

    # Create the relationship in UserBook
    new_user_book = UserBook(user_book_u_id=data.user_id, user_book_b_id=data.book_id)
    db.add(new_user_book)
    db.commit()

    return {
        "user_id": data.user_id,
        "book_id": data.book_id
    }


