from fastapi import APIRouter, Depends
from sqlite.database import get_db
from sqlalchemy.orm import Session
from users.schemas import UserRequest, UserResponse, LoginRequest
from sqlite import db_user

router = APIRouter(
  prefix='/api/user',
  tags=['user']
)

@router.post("/create", response_model=UserResponse)
async def create_user(request: UserRequest, db: Session = Depends(get_db)):
    return db_user.create(db, request)

@router.post("/login", response_model=UserResponse)
async def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    return db_user.login(db, request)