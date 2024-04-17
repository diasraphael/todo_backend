from fastapi import APIRouter, Depends
from sqlite.database import get_db
from sqlalchemy.orm import Session
from tasks.schemas import TaskResponse, TaskRequest
from tasks import db_repository

task_router = APIRouter(prefix="/api/task-entry", tags=["task"])


@task_router.post("/create", response_model=TaskResponse)
async def create_task_entry(request: TaskRequest, db: Session = Depends(get_db)):
    return db_repository.create_task_entry(db, request)
