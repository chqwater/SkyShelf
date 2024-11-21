from app.models import UserInf
from app import models, schemas
from sqlalchemy.orm import Session


# 创建书籍
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        book_name=book.book_name,
        book_url=book.book_url,
        a_id=book.a_id  # 关联作者ID
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# 获取书籍列表
def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

# 创建用户
def create_user(db: Session, user: schemas.UserInfCreate):
    db_user = models.UserInf(
        user_email=user.user_email,
        user_name=user.user_name,
        user_password=user.user_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 根据 email 查询用户并验证密码
def get_user_by_email(db: Session, email: str, password: str):
    user = db.query(UserInf).filter(UserInf.user_email == email).first()
    if user and password == user.user_password:  # 验证密码
        return user
    return None