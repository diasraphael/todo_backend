from datetime import datetime, timedelta, timezone
import re
from typing import Union
from fastapi import HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


# openssl rand -hex 32
SECRET_KEY = "469c4ba773f89487308c9c79247372c994dbd244eebf872c06375e148ff39f5b"

ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user_from_token(request: Request):
    token = request.cookies.get("access_token")
    print("I am the access token", token, request.cookies)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        # headers={"WWW-Authenticate": "Bearer"},
    )
    if not token:
        raise credentials_exception
    """ if token.lower().startswith("bearer "):
        token = token[7:] """
    try:
        print("I am the token", token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception

    user_id: str = payload.get("user")
    print("I am the user id", user_id, request.cookies, request)
    if user_id is None:
        raise credentials_exception
    return user_id
