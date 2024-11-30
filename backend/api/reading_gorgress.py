from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, create_engine, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base


router = APIRouter()
# Initialize FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database model (mapping to existing table)
class UserBook(Base):
    __tablename__ = "User_book"  # Existing table name
    user_book_id = Column(Integer, primary_key=True, index=True)
    user_book_u_id = Column(Integer, nullable=False)
    user_book_b_id = Column(Integer, nullable=False)
    last_read_time = Column(DateTime, nullable=True, default=datetime.utcnow)
    last_read_position = Column(Integer, nullable=False, default=1)

# Request body model
class ReadingProgress(BaseModel):
    user_id: int = Field(..., description="The ID of the user")
    book_id: int = Field(..., description="The ID of the book")
    last_read_position: int = Field(..., description="The last read position in the book")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/reading_progress")
async def save_reading_progress(data: ReadingProgress, db: SessionLocal = Depends(get_db)):
    # Check if user-book pair exists
    user_book = db.query(UserBook).filter_by(user_book_u_id=data.user_id, user_book_b_id=data.book_id).first()

    if user_book:
        # Update the last_read_position
        user_book.last_read_position = data.last_read_position
        user_book.last_read_time = datetime.utcnow()
        db.commit()
        return {
            "user_id": user_book.user_book_u_id,
            "book_id": user_book.user_book_b_id,
            "last_read_position": user_book.last_read_position,
            "last_read_time": user_book.last_read_time
        }
    else:
        # Record does not exist
        raise HTTPException(status_code=404, detail="User or book not found")


