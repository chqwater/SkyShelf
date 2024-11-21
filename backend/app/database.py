from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 替换为你的数据库连接 URL
DATABASE_URL = "mysql+pymysql://team_skyshelf:SkyShelf2024@db4free.net:3306/skyshelf_sdm"

# 创建数据库引擎
engine = create_engine(DATABASE_URL)  # 不需要 SQLite 的特殊配置

# 配置数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 定义基础模型类
Base = declarative_base()

# 数据库会话依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
