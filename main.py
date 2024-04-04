from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlite.database import engine
from sqlite import models
from routers import user, task

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

app.include_router(user.router)
app.include_router(task.router)

models.Base.metadata.create_all(engine)
