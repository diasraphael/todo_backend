from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    email: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True  # this helps in converting the database type to the type we need to show to the user


class UserRequest(BaseModel):
    username: str
    password: str
    email: str


class LoginRequest(BaseModel):
    password: str
    email: str
