from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    title: str
    class Config():
        from_attributes = True

class TaskRequest(BaseModel):
    title: str
    user_id: int

class TaskResponse(BaseModel):
    title: str
    user_id: int
    id: int
    class Config():
        from_attributes = True


class User(BaseModel):
    username: str
    password: str
    email: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    tasks: List[Task] = []
    class Config():
        from_attributes = True   # this helps in converting the database type to the type we need to show to the user

class UserRequest(BaseModel):
    username: str
    password: str
    email: str

class LoginRequest(BaseModel):
    password: str
    email: str
    