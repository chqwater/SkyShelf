from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime
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
    description = Column(String, nullable=False)  # Add the missing 'description' field

class UserBook(Base):
    __tablename__ = "User_book"
    user_book_id = Column(Integer, primary_key=True, index=True)
    user_book_u_id = Column(Integer, ForeignKey("User_inf.user_id"), nullable=False)
    user_book_b_id = Column(Integer, ForeignKey("Book.book_id"), nullable=False)
    last_read_time = Column(DateTime, nullable=True, default=datetime.utcnow)
    last_read_position = Column(Integer, nullable=True, default=1)

class BookCategories(Base):
    __tablename__ = "Book_categories"
    b_id = Column(Integer, ForeignKey("Book.book_id"), primary_key=True, index=True)
    c_id = Column(Integer, ForeignKey("Categories.categories_id"), primary_key=True, index=True)


class UserSelectedCategories(Base):
    __tablename__ = "User_selected_categories"

    u_id = Column(Integer, ForeignKey("User_inf.user_id"), primary_key=True)  # Primary key on user_id
    c_id = Column(Integer, ForeignKey("Categories.categories_id"), primary_key=True)  # Primary key on categories_id

    # Optionally, you can add other fields like 'created_at', etc.
    # created_at = Column(DateTime, default=datetime.utcnow)

@router.post("/api/admin/delete-book")
async def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a book by its ID, along with all related records in UserBook, BookCategories, and UserSelectedCategories.
    """
    try:
        book = db.query(Book).filter(Book.book_id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

        db.query(UserBook).filter(UserBook.user_book_b_id == book_id).delete()

        db.query(BookCategories).filter(BookCategories.b_id == book_id).delete()

        db.query(UserSelectedCategories).filter(UserSelectedCategories.u_id == book_id).delete()

        db.delete(book)

        db.commit()

        return {"message": f"The book with ID {book_id} has been deleted successfully."}

    except SQLAlchemyError as e:
        db.rollback()  # Rollback the transaction in case of an error
        raise HTTPException(status_code=500, detail="A database error occurred.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")