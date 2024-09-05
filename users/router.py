from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from util.auth import create_access_token
from db.database import get_db
from sqlalchemy.orm import Session
from users.schemas import (
    AuthenticatedResponse,
    UserRequest,
    LoginRequest,
)
from users import db_repository


user_router = APIRouter(prefix="/api/user", tags=["user"])


ACCESS_TOKEN_EXPIRE_MINUTES = 30


def formatUserResponse(user, response: JSONResponse):
    print("formatUserResponse", user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Try different username or password",
            #  headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"user": user.id}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="None",
        secure=True,
    )
    """ response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="Lax",
        secure=False,
    ) """
    return {"user": user}
    # store token in a cookie instead of sending it back as JSON
    # make sure to set the cookie settings to "secure" and "httpOnly"
    # Response object from FastAPI can be used to set cookies
    # The httponly and secure parameters are set to True to prevent the cookie from being accessed through client-side scripts and to ensure that the cookie is only sent over HTTPS


@user_router.post("/create", response_model=AuthenticatedResponse)
async def create_user(
    request: UserRequest,
    response: JSONResponse,
    db: Session = Depends(get_db),
):
    user = db_repository.create(db, request)
    return formatUserResponse(user, response)


@user_router.post("/login", response_model=AuthenticatedResponse)
async def login_user(
    request: LoginRequest,
    response: JSONResponse,
    db: Session = Depends(get_db),
):
    user = db_repository.login(db, request)
    return formatUserResponse(user, response)


@user_router.get("/hello")
async def hello_world():
    return {"message": "Hello, World!"}
