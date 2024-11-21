from sqlalchemy import Column, String, Integer, BigInteger, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Author 表
class Author(Base):
    __tablename__ = 'Author'

    author_id = Column(BigInteger, primary_key=True, autoincrement=True)
    author_name = Column(String(255), nullable=False)

# Book 表
class Book(Base):
    __tablename__ = 'Book'

    book_id = Column(BigInteger, primary_key=True, autoincrement=True)
    book_name = Column(String(255), nullable=True)
    book_url = Column(String(255), nullable=True)
    a_id = Column(BigInteger, ForeignKey('Author.author_id'), nullable=False)

    # 定义外键关系
    author = relationship('Author', backref='books')

# Book_categories 表（多对多关系表）
class BookCategories(Base):
    __tablename__ = 'Book_categories'

    b_id = Column(BigInteger, ForeignKey('Book.book_id'), primary_key=True)  # 外键且为主键
    c_id = Column(BigInteger, ForeignKey('Categories.categories_id'), primary_key=True)  # 外键且为主键


# Categories 表
class Categories(Base):
    __tablename__ = 'Categories'

    categories_id = Column(BigInteger, primary_key=True, autoincrement=True)
    categories_name = Column(String(255), nullable=False)

# User_book 表（多对多关系表）
class UserBook(Base):
    __tablename__ = 'User_book'

    user_book_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_u_id = Column(BigInteger, ForeignKey('User_inf.user_id'), nullable=False)
    user_b_id = Column(BigInteger, ForeignKey('Book.book_id'), nullable=False)
    last_read_time = Column(Date, nullable=True)
    last_read_position = Column(Integer, nullable=True)

    # 定义外键关系
    user = relationship('UserInf', backref='user_books')
    book = relationship('Book', backref='user_books')

# User_inf 表
class UserInf(Base):
    __tablename__ = 'User_inf'

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_email = Column(String(255), unique=True, nullable=False)
    user_name = Column(String(255), nullable=False)
    user_password = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False, default="user")

# User_selected_categories 表（多对多关系表）
class UserSelectedCategories(Base):
    __tablename__ = 'User_selected_categories'

    u_c_id = Column(BigInteger, ForeignKey('User_inf.user_id'), nullable=True, primary_key=True)
    c_id = Column(BigInteger, ForeignKey('Categories.categories_id'), nullable=True, primary_key=True)
