from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends, APIRouter, Path
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Enum, DateTime, Boolean
from sqlalchemy.exc import SQLAlchemyError
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
class UserInf(Base):
    __tablename__ = "User_inf"
    user_id = Column(Integer, primary_key=True, index=True)

class Book(Base):
    __tablename__ = "Book"
    book_id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String(255), nullable=False)
    book_url = Column(String(255), nullable=False)
    img_url = Column(String(255), nullable=False)

class UserBook(Base):
    __tablename__ = "User_book"
    user_book_id = Column(Integer, primary_key=True, index=True)
    user_book_u_id = Column(Integer, ForeignKey("User_inf.user_id"), nullable=False)
    user_book_b_id = Column(Integer, ForeignKey("Book.book_id"), nullable=False)
    last_read_time = Column(DateTime, nullable=True, default=datetime.utcnow)
    last_read_position = Column(Integer, nullable=True, default=1)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/shelf/{user_id}")
async def get_user_shelf(
        user_id: int = Path(..., title="The ID of the user to get recommendations for"),
    db: SessionLocal = Depends(get_db)
):
    try:
        # Check if the user exists
        user = db.query(UserInf).filter(UserInf.user_id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

        user_books = db.query(UserBook).filter(UserBook.user_book_u_id == user_id).all()
        if not user_books:
            return []
        shelf = []
        for user_book in user_books:
            book = db.query(Book).filter(Book.book_id == user_book.user_book_b_id).first()
            if book:
                shelf.append({
                    "book_id": book.book_id,
                    "book_name": book.book_name,
                    "file_url": book.book_url,
                    "img_url": book.img_url,
                    "currentPage": user_book.last_read_position
                })
        return shelf
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

