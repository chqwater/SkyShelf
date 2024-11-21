from fastapi import FastAPI
from app.routers import user  # 导入用户模块的路由
from app.database import Base, engine

# 初始化数据库
Base.metadata.create_all(bind=engine)

# 创建 FastAPI 实例
app = FastAPI()

# 注册路由
app.include_router(user.router)
