from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from util.auth import create_access_token
from sqlite.database import get_db
from sqlalchemy.orm import Session
from users.schemas import (
    AuthenticatedResponse,
    UserRequest,
    LoginRequest,
)
from users import db_repository


user_router = APIRouter(prefix="/api/user", tags=["user"])


ACCESS_TOKEN_EXPIRE_MINUTES = 30


def formatUserResponse(user):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Try different username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # store token in a cookie instead of sending it back as JSON
    # amke sure to set the cookie settings to "secure" and "httpOnly"
    return {
        "user": user,
        "token": {
            "access_token": create_access_token(
                data={"user": user.id}, expires_delta=access_token_expires
            ),
            "token_type": "bearer",
        },
    }


@user_router.post("/create", response_model=AuthenticatedResponse)
async def create_user(
    request: UserRequest,
    db: Session = Depends(get_db),
):
    user = db_repository.create(db, request)
    return formatUserResponse(user)


@user_router.post("/login", response_model=AuthenticatedResponse)
async def login_user(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    user = db_repository.login(db, request)
    return formatUserResponse(user)
