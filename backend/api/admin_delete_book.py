from fastapi import FastAPI, HTTPException, Depends, APIRouter, Path
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Enum, DateTime, Boolean
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

router = APIRouter()

# Database Configuration
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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

@router.post("/api/admin/delete-book")
async def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a book by its ID.
    """
    try:
        # Check if the book exists
        book = db.query(Book).filter(Book.book_id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

        # Delete associated entries in UserBook table
        db.query(UserBook).filter(UserBook.book_id == book_id).delete()

        # Delete the book entry
        db.delete(book)

        # Commit the changes
        db.commit()

        return {"message": f"The book with ID {book_id} has been deleted successfully."}

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="A database error occurred.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")