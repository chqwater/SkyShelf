from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, model_validator
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Initialize FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database model
class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String(255), nullable=True)
    author_name = Column(String(255), nullable=True)
    file_url = Column(String(255), nullable=True)
    img_url = Column(String(255), nullable=True)
    description = Column(String(500), nullable=True)
    category_id = Column(Integer, nullable=True)

# Request body model
class EditBookRequest(BaseModel):
    book_id: int = Field(..., description="The ID of the book to edit")
    book_name: str = Field(None, description="The new name of the book")
    author_name: str = Field(None, description="The new author name")
    file_url: str = Field(None, description="The new file URL for the book")
    img_url: str = Field(None, description="The new image URL for the book cover")
    description: str = Field(None, description="The new description for the book")
    category_id: int = Field(None, description="The new category ID for the book")

    @model_validator(mode="after")
    def at_least_one_field(cls, values):
        """Ensure at least one field besides book_id is provided for updating."""
        editable_fields = ["book_name", "author_name", "file_url", "img_url", "description", "category_id"]
        if not any(values.get(field) for field in editable_fields):
            raise ValueError("At least one field to edit must be provided.")
        return values

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/admin/edit-book")
async def edit_book(data: EditBookRequest, db: SessionLocal = Depends(get_db)):
    # Check if the book exists
    book = db.query(Book).filter_by(id=data.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Update the specified fields
    updates = {}
    if data.book_name:
        updates["book_name"] = data.book_name
    if data.author_name:
        updates["author_name"] = data.author_name
    if data.file_url:
        updates["file_url"] = data.file_url
    if data.img_url:
        updates["img_url"] = data.img_url
    if data.description:
        updates["description"] = data.description
    if data.category_id:
        updates["category_id"] = data.category_id

    # Perform the update
    db.query(Book).filter_by(id=data.book_id).update(updates)
    db.commit()

    return {"message": "Edit successfully!"}
