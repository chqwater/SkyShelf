from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/api", tags=["Users"])

@router.post("/login", response_model=schemas.LoginResponse)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    # 查询用户是否是管理员
    db_user = crud.get_user_by_email(db, email=user.email, password=user.password)

    if db_user:
        # 判断用户角色，返回角色信息
        return {"user_id": db_user.user_id ,"role": db_user.role, "message": f"Welcome {db_user.user_name} ({db_user.role.capitalize()})!"}

    raise HTTPException(status_code=401, detail="Invalid credentials")