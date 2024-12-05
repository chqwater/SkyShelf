from fastapi import FastAPI, HTTPException, Depends
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
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String(255), nullable=False, unique=True)
    user_name = Column(String(255), nullable=False)
    user_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/admin/users")
async def get_all_users(db: SessionLocal = Depends(get_db)):
    """
    Retrieve all users with specific fields.
    """
    try:
        users = db.query(User).all()  # Fetch all users
        user_list = []
        for user in users:
            user_list.append({
                "user_id": user.id,
                "user_name": user.user_name,
                "email": user.user_email,
                "password": user.user_password,  # Encrypted password as stored in DB
                "role": user.role
            })
        return {"users": user_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching users: {str(e)}")
