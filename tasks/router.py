from fastapi import APIRouter, Depends, status
from sqlite.database import get_db
from sqlalchemy.orm import Session
from tasks.schemas import TaskResponse, TaskRequest
from tasks import db_repository
from typing import List

task_router = APIRouter(prefix="/api/tasks", tags=["task"])


@task_router.get("/", response_model=List[TaskResponse])
async def get_tasks(db: Session = Depends(get_db)):
    return db_repository.get(db)


@task_router.post("/create", response_model=TaskResponse)
async def create_task(request: TaskRequest, db: Session = Depends(get_db)):
    return db_repository.create(db, request)


@task_router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: int, db: Session = Depends(get_db)):
    return db_repository.delete(db, id)
