from fastapi import FastAPI, HTTPException, Path, Depends, APIRouter
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Enum
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError
from typing import List
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
    a_id = Column(Integer, ForeignKey("Author.author_id"), nullable=False)
    description = Column(String, nullable=False)
    book_url = Column(String(255), nullable=False)
    img_url = Column(String(255), nullable=False)
    # Relationship to BookCategories
    categories = relationship("BookCategories", back_populates="book")

class Author(Base):
    __tablename__ = "Author"
    author_id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String(255), nullable=False)

class BookCategories(Base):
    __tablename__ = "Book_categories"
    b_id = Column(Integer, ForeignKey("Book.book_id"), primary_key=True, index=True)
    c_id = Column(Integer, ForeignKey("Categories.categories_id"), primary_key=True, index=True)
    # Relationships
    book = relationship("Book", back_populates="categories")
    category = relationship("Categories", back_populates="books")

class Categories(Base):
    __tablename__ = "Categories"
    categories_id = Column(Integer, primary_key=True, index=True)
    categories_name = Column(String(255), nullable=False)
    # Relationship to BookCategories
    books = relationship("BookCategories", back_populates="category")



@router.get("/api/admin/books")
async def get_books(
    category_id: int = None,  # Optional query parameter for category filtering
    db: Session = Depends(get_db)
):
    try:
        # Base query
        books_query = db.query(
            Book.book_id,
            Book.book_name,
            Book.description,
            Book.book_url,
            Book.img_url,
            Author.author_name,
            Categories.categories_id,
            Categories.categories_name
        ).join(
            BookCategories, Book.book_id == BookCategories.b_id
        ).join(
            Categories, BookCategories.c_id == Categories.categories_id
        ).join(
            Author, Book.a_id == Author.author_id
        )

        # Apply category filter if category_id is provided
        if category_id:
            books_query = books_query.filter(Categories.categories_id == category_id)

        # Execute the query and fetch results
        books = books_query.all()

        # Transform results into desired format
        books_list = [
            {
                "book_id": book.book_id,
                "title": book.book_name,
                "author": book.author_name,
                "description": book.description,
                "file_url": book.book_url,
                "img_url": book.img_url,
                "category_id": book.categories_id,
                "category_name": book.categories_name
            }
            for book in books
        ]

        # Response
        return {"books": books_list}

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


