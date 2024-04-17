from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlite.database import engine
from users import models as usersModels
from tasks import models as tasksModels
from users.router import user_router
from tasks.router import task_router

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

app.include_router(user_router)
app.include_router(task_router)

usersModels.Base.metadata.create_all(engine)
tasksModels.Base.metadata.create_all(engine)
