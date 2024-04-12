from fastapi import APIRouter, Depends
from sqlite.database import get_db
from sqlalchemy.orm import Session
from users.schemas import UserRequest, UserResponse, LoginRequest
from users import db_repository

user_router = APIRouter(prefix="/api/user", tags=["user"])


@user_router.post("/create", response_model=UserResponse)
async def create_user(request: UserRequest, db: Session = Depends(get_db)):
    return db_repository.create(db, request)


@user_router.post("/login", response_model=UserResponse)
async def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return db_repository.login(db, request)
