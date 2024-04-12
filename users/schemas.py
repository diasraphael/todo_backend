from pydantic import BaseModel
from typing import List
from tasks.schemas import Task


class User(BaseModel):
    username: str
    password: str
    email: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    tasks: List[Task] = []

    class Config:
        from_attributes = True  # this helps in converting the database type to the type we need to show to the user


class UserRequest(BaseModel):
    username: str
    password: str
    email: str


class LoginRequest(BaseModel):
    password: str
    email: str
