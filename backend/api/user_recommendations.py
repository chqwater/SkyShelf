from fastapi import FastAPI, HTTPException, Path, Depends, APIRouter
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Enum
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
class UserInf(Base):
    __tablename__ = "User_inf"
    user_id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum("user", "admin", name="user_role"), nullable=False)
    user_email = Column(String(255), unique=True, nullable=False)
    user_password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    selected_categories = relationship("UserSelectedCategories", back_populates="user")


class Journey(Base):
    __tablename__ = "Categories"
    categories_id = Column(Integer, primary_key=True, index=True)
    categories_name = Column(String(255), nullable=False)
    books = relationship("BookCategories", back_populates="journey")
    selected_by_users = relationship("UserSelectedCategories", back_populates="journey")

class UserSelectedCategories(Base):
    __tablename__ = "User_selected_categories"
    u_id = Column(Integer, ForeignKey("User_inf.user_id"), primary_key=True, index=True)
    c_id = Column(Integer, ForeignKey("Categories.categories_id"), primary_key=True, index=True)
    journey = relationship("Journey", back_populates="selected_by_users")
    user = relationship("UserInf", back_populates="selected_categories")

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
    journey = relationship("Journey", back_populates="books")
    book = relationship("Book", back_populates="categories")


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/recommendation/{u_id}")
async def get_recommendations(
    u_id: int = Path(..., title="The ID of the user to get recommendations for"),
    db: SessionLocal = Depends(get_db)
):
    try:
        # Check if the user exists
        user = db.query(UserInf).filter(UserInf.user_id == u_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id {u_id} not found")

        # Get selected categories for the user
        selected_categories = db.query(UserSelectedCategories).filter(UserSelectedCategories.u_id == u_id).all()
        selected_journey_ids = {category.c_id for category in selected_categories}

        # Get all journeys
        journeys = db.query(Journey).all()
        if len(journeys) != 10:
            raise HTTPException(status_code=500, detail="The total number of journeys must be 10")

        # Recommendations for selected journeys
        selected_recommendations = []
        for journey in journeys:
            if journey.categories_id in selected_journey_ids:
                books = (
                    db.query(Book)
                    .join(BookCategories, Book.book_id == BookCategories.b_id)
                    .filter(BookCategories.c_id == journey.categories_id)
                    .limit(3)
                    .all()
                )
                selected_recommendations.append({
                    "id": journey.categories_id,
                    "name": journey.categories_name,
                    "books": [{
                        "id": book.book_id,
                        "title": book.book_name,
                        "author": db.query(Author.author_name).filter(Author.author_id == book.a_id).scalar(),
                        "description": book.description,
                        "file_url": book.book_url,
                        "img_url": book.img_url
                    } for book in books]
                })

        # Recommendations for unselected journeys
        unselected_recommendations = []
        for journey in journeys:
            if journey.categories_id not in selected_journey_ids:
                books = (
                    db.query(Book)
                    .join(BookCategories, Book.book_id == BookCategories.b_id)
                    .filter(BookCategories.c_id == journey.categories_id)
                    .limit(3)
                    .all()
                )
                unselected_recommendations.append({
                    "id": journey.categories_id,
                    "name": journey.categories_name,
                    "books": [{
                        "id": book.book_id,
                        "title": book.book_name,
                        "author": db.query(Author.author_name).filter(Author.author_id == book.a_id).scalar(),
                        "description": book.description,
                        "file_url": book.book_url,
                        "img_url": book.img_url
                    } for book in books]
                })

        recommendations = selected_recommendations + unselected_recommendations
        return {"recommendations": recommendations}

    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database error occurred")
    except Exception:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")