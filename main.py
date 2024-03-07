from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uuid
import bcrypt


class User(BaseModel):
    user_id: str
    username: str
    password: str
    email: str


class PublicUser(BaseModel):
    user_id: str
    username: str
    email: str


class CreatePublicUser(BaseModel):
    username: str
    password: str
    email: str


app = FastAPI()

# Allow requests from http://localhost:3000
origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

users = [
    {
        "user_id": "99f4df04-4c15-46e8-a8de-f053a782607f",
        "username": "Dias",
        "password": "$2b$12$FwDDzjskjI5tQlpF4gqc1um8ZJzWqHDvC2.BmBqA/kycAokC5ig.q",
        "email": "diasraphael88@gmail.com",
    }
]


@app.post("/api/user")
async def create_user(user: CreatePublicUser):
    user_id = str(uuid.uuid4())
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    new_user = User(
        user_id=user_id,
        password=hashed_password.decode("utf-8"),
        **user.dict(exclude={"user_id", "password"})
    )
    users.append(new_user.dict())
    return new_user


@app.post("/api/login")
async def login_user(user: User):
    for existing_user in users:
        if existing_user["email"] == user.email and bcrypt.checkpw(
            user.password.encode("utf-8"), existing_user["password"].encode("utf-8")
        ):
            return existing_user
    return {"error": "Invalid username or password"}
