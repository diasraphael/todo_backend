from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlite.database import engine
from sqlite import models
from sqlite.database import get_db
from sqlalchemy.orm import Session
from sqlite.schemas import UserRequest, UserResponse, LoginRequest, User
from sqlite import db_user

app = FastAPI()

# Allow requests from http://localhost:3000
origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.post("/api/user", response_model=UserResponse)
async def create_user(request: UserRequest, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@app.get("/api/users", response_model=List[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


@app.post("/api/login", response_model=UserResponse)
async def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return db_user.login_user(db, request)


models.Base.metadata.create_all(engine)
