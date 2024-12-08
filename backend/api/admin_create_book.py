from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, create_engine, select, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

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
    categories = relationship("BookCategories", back_populates="book")

class Author(Base):
    __tablename__ = "Author"
    author_id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String(255), nullable=False)

class BookCategories(Base):
    __tablename__ = "Book_categories"
    b_id = Column(Integer, ForeignKey("Book.book_id"), primary_key=True, index=True)
    c_id = Column(Integer, ForeignKey("Categories.categories_id"), primary_key=True, index=True)
    book = relationship("Book", back_populates="categories")
    category = relationship("Categories", back_populates="book_categories")  # Updated relationship

class Categories(Base):
    __tablename__ = "Categories"
    categories_name = Column(String(255), nullable=False)
    categories_id = Column(Integer, primary_key=True, index=True)
    book_categories = relationship("BookCategories", back_populates="category")  # Updated relationship


# Define the CreateBookRequest Pydantic schema for the incoming request
class CreateBookRequest(BaseModel):
    book_name: str
    book_url: str
    author_name: str
    img_url: str
    description: str
    category_id: int


@router.post("/api/admin/create-book")
async def create_book(book_request: CreateBookRequest, db: Session = Depends(get_db)):
    try:
        # Step 1: Check if the author exists
        author = db.query(Author).filter(Author.author_name == book_request.author_name).first()
        
        # If the author does not exist, create a new one
        if not author:
            new_author = Author(author_name=book_request.author_name)
            db.add(new_author)
            db.commit()
            db.refresh(new_author)
            author_id = new_author.author_id
        else:
            author_id = author.author_id
        
        # Step 2: Create the new book
        new_book = Book(
            book_name=book_request.book_name,
            book_url=book_request.book_url,
            a_id=author_id,  # linking to the author
            img_url=book_request.img_url,
            description=book_request.description
        )
        db.add(new_book)
        db.commit()
        db.refresh(new_book)

        # Step 3: Link the book with the category (via BookCategories table)
        book_category = BookCategories(b_id=new_book.book_id, c_id=book_request.category_id)
        db.add(book_category)
        db.commit()

        # Return success message with book details
        return {
            "message": "Book created successfully!",
            "book_name": new_book.book_name,
            "book_url": new_book.book_url,
            "author_id": author_id,
            "img_url": new_book.img_url,
            "description": new_book.description,
            "category_id": book_request.category_id
        }

    except SQLAlchemyError as e:
        db.rollback()  # Rollback the transaction in case of error
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")    