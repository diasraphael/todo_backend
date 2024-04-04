from fastapi import APIRouter, Depends
from sqlite.database import get_db
from sqlalchemy.orm import Session
from sqlite.schemas import TaskResponse, TaskRequest
from sqlite import db_task

router = APIRouter(
  prefix='/api/task',
  tags=['task']
)

@router.post("/", response_model=TaskResponse)
async def create_task(request: TaskRequest, db: Session = Depends(get_db)):
    return db_task.create(db, request)