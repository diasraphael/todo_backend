from fastapi import APIRouter, Depends, status
from util.auth import get_user_from_token
from db.database import get_db
from sqlalchemy.orm import Session
from tasks.schemas import TaskResponse, TaskRequest
from tasks import db_repository
from typing import List

task_router = APIRouter(prefix="/api/tasks", tags=["task"])


@task_router.get("/", response_model=List[TaskResponse])
async def get_tasks(
    user_id: str = Depends(get_user_from_token),
    db: Session = Depends(get_db),
):
    return db_repository.get_tasks(db, user_id)


@task_router.post("/", response_model=TaskResponse)
async def create_task(
    request: TaskRequest,
    user_id: str = Depends(get_user_from_token),
    db: Session = Depends(get_db),
):
    task_request = TaskRequest(title=request.title, userId=user_id)
    return db_repository.create(db, task_request)


@task_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    id: int, user_id: str = Depends(get_user_from_token), db: Session = Depends(get_db)
):
    return db_repository.delete(db, id)
