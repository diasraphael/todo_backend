from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    email: str


class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    class Config():
        from_attributes = True

class UserRequest(BaseModel):
    username: str
    password: str
    email: str

class LoginRequest(BaseModel):
    password: str
    email: str
    