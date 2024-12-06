from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel, Field, model_validator
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Initialize FastAPI app
router = APIRouter()

# Database configuration
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database model
class Book(Base):
    __tablename__ = "Book"
    book_id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String(255), nullable=True)
    a_id = Column(Integer, ForeignKey("Author.author_id"), nullable=False)
    book_url = Column(String(255), nullable=True)
    img_url = Column(String(255), nullable=True)
    description = Column(String(500), nullable=True)
    categories = relationship("BookCategories", back_populates="book")

class Category(Base):
    __tablename__ = "Categories"
    categories_id = Column(Integer, primary_key=True, index=True)
    categories_name = Column(String(255), nullable=False)  # Added length to VARCHAR
    books = relationship("BookCategories", back_populates="journey")

class BookCategories(Base):
    __tablename__ = "Book_categories"
    b_id = Column(Integer, ForeignKey("Book.book_id"), primary_key=True, index=True)
    c_id = Column(Integer, ForeignKey("Categories.categories_id"), primary_key=True, index=True)
    journey = relationship("Category", back_populates="books")
    book = relationship("Book", back_populates="categories")

class Author(Base):
    __tablename__ = "Author"
    author_id = Column(Integer, primary_key=True, index=True)
    author_name = Column(String(255), nullable=False)

# Request body model
class EditBookRequest(BaseModel):
    book_id: int = Field(..., description="The ID of the book to edit")
    book_name: str = Field(None, description="The new name of the book")
    author_name: str = Field(None, description="The new author name")
    book_url: str = Field(None, description="The new file URL for the book")
    img_url: str = Field(None, description="The new image URL for the book cover")
    description: str = Field(None, description="The new description for the book")
    category_id: int = Field(None, description="The new category ID for the book")

    @model_validator(mode="after")
    def at_least_one_field(cls, model):
        """Ensure at least one field besides book_id is provided for updating."""
        editable_fields = [
            model.book_name,
            model.author_name,
            model.book_url,
            model.img_url,
            model.description,
            model.category_id,
        ]
        if not any(editable_fields):
            raise ValueError("At least one field to edit must be provided.")
        return model

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/admin/edit-book")
async def edit_book(data: EditBookRequest, db: SessionLocal = Depends(get_db)):
    # Check if the book exists
    book = db.query(Book).filter(Book.book_id == data.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Update book fields
    if data.book_name:
        book.book_name = data.book_name
    if data.book_url:
        book.book_url = data.book_url
    if data.img_url:
        book.img_url = data.img_url
    if data.description:
        book.description = data.description

    # Update author
    if data.author_name:
        # Check if the author already exists
        author = db.query(Author).filter(Author.author_name == data.author_name).first()
        if not author:
            # Create a new author if it doesn't exist
            author = Author(author_name=data.author_name)
            db.add(author)
            db.commit()
            db.refresh(author)
        # Associate the book with the new/existing author
        book.a_id = author.author_id

    # Update category
    if data.category_id:
        # Check if the category exists
        category = db.query(Category).filter(Category.categories_id == data.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        # Remove any existing category associations for the book
        db.query(BookCategories).filter(BookCategories.b_id == data.book_id).delete()

        # Create a new association between the book and the new category
        book_category = BookCategories(b_id=data.book_id, c_id=data.category_id)
        db.add(book_category)

    # Commit the changes
    db.commit()

    return {"message": "Edit successfully!"}
