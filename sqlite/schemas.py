from pydantic import BaseModel
from typing import List,Optional

class Task(BaseModel):
    title: str
    class Config():
        orm_mode = True

class TaskRequest(BaseModel):
    title: str
    user_id: int

class TaskResponse(BaseModel):
    title: str
    user_id: int
    task_id: int
    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    password: str
    email: str

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    tasks: Optional[List[Task]] = None
    class Config():
        orm_mode = True

class UserRequest(BaseModel):
    username: str
    password: str
    email: str

class LoginRequest(BaseModel):
    password: str
    email: str
    