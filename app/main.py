
from fastapi import Depends, FastAPI
from app.auth.router import auth_router


import uvicorn

app = FastAPI()


app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info",port=8089)