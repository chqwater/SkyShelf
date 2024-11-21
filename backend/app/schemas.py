from pydantic import BaseModel
from typing import Optional, List

# Book Schema
class BookBase(BaseModel):
    book_name: Optional[str]
    book_url: Optional[str]
    a_id: int  # author_id (Foreign Key)

class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int

    class Config:
        from_attributes = True

# Categories Schema
class CategoriesBase(BaseModel):
    categories_name: str

class CategoriesCreate(CategoriesBase):
    pass

class Categories(CategoriesBase):
    categories_id: int

    class Config:
        from_attributes = True

# BookCategories Schema (For many-to-many relationship)
class BookCategoriesBase(BaseModel):
    b_id: int  # book_id
    c_id: int  # categories_id

class BookCategoriesCreate(BookCategoriesBase):
    pass

class BookCategories(BookCategoriesBase):
    class Config:
        from_attributes = True

# UserBook Schema (For many-to-many relationship)
class UserBookBase(BaseModel):
    user_u_id: int  # user_id
    user_b_id: int  # book_id
    last_read_time: Optional[str]  # date
    last_read_position: Optional[int]

class UserBookCreate(UserBookBase):
    pass

class UserBook(UserBookBase):
    user_book_id: int

    class Config:
        from_attributes = True

# UserInf Schema
class UserInfBase(BaseModel):
    user_email: str
    user_name: str
    user_password: str

class UserInfCreate(UserInfBase):
    pass

class UserInf(UserInfBase):
    user_id: int

    class Config:
        from_attributes = True

# UserSelectedCategories Schema (For many-to-many relationship)
class UserSelectedCategoriesBase(BaseModel):
    u_c_id: int  # user_id
    c_id: int  # categories_id

class UserSelectedCategoriesCreate(UserSelectedCategoriesBase):
    pass

class UserSelectedCategories(UserSelectedCategoriesBase):
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    user_id: int
    role: str
    message: str
