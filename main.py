from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from users import models as usersModels
from tasks import models as tasksModels
from task_entry import models as taskEntryModels
from users.router import user_router
from tasks.router import task_router
from task_entry.router import task_entry_router
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Allow requests from http://localhost:3000
origins = ["http://localhost:3001", "http://127.0.0.1:3001"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(user_router)
app.include_router(task_router)
app.include_router(task_entry_router)

usersModels.Base.metadata.create_all(engine)
tasksModels.Base.metadata.create_all(engine)
taskEntryModels.Base.metadata.create_all(engine)
