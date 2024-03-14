from typing import List
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlite.database import engine
from sqlite import models
from sqlite.database import get_db
from sqlalchemy.orm import Session
from sqlite.schemas import UserRequest,UserResponse,LoginRequest,User
from sqlite import db_user

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

""" users = [
    {
        "user_id": "99f4df04-4c15-46e8-a8de-f053a782607f",
        "username": "Dias",
        "password": "$2b$12$FwDDzjskjI5tQlpF4gqc1um8ZJzWqHDvC2.BmBqA/kycAokC5ig.q",
        "email": "diasraphael88@gmail.com",
    }
] """



""" @app.post("/api/user")
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
    return {"error": "Invalid username or password"} """


@app.post("/api/user", response_model=UserResponse)
async def create_user(request: UserRequest,db: Session=Depends(get_db)):
    return db_user.create_user(db,request)

@app.get("/api/users", response_model=List[UserResponse])
async def get_all_users(db: Session=Depends(get_db)):
    return db_user.get_all_users(db)

@app.post("/api/login", response_model=UserResponse)
async def login_user(request: LoginRequest,db: Session=Depends(get_db)):
    return db_user.login_user(db,request)

models.Base.metadata.create_all(engine)