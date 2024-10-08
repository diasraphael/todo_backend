from typing import List
from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from task_entry.schemas import TaskEntryResponse, TaskEntryRequest
from task_entry import db_repository
from util.auth import get_user_from_token

task_entry_router = APIRouter(prefix="/api/task-entry", tags=["task-entry"])


@task_entry_router.post("/", response_model=TaskEntryResponse)
async def create_task_entry(
    request: TaskEntryRequest,
    user_id: str = Depends(get_user_from_token),
    db: Session = Depends(get_db),
):
    return db_repository.create_task_entry(db, request)


@task_entry_router.get("/", response_model=List[TaskEntryResponse])
async def get_task_entries_by_user(
    user_id: str = Depends(get_user_from_token),
    db: Session = Depends(get_db),
):
    return db_repository.get_task_entries_by_user(db, user_id)
