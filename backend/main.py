import uvicorn
from app.main import app  # 引用 app 文件夹中的主应用

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
