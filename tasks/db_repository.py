from .models import Task
from sqlalchemy.orm.session import Session
from .schemas import TaskRequest, TaskResponse
from sqlalchemy.exc import IntegrityError
from typing import List


def get_tasks(db: Session, user_id: int) -> List[TaskResponse]:
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks


def create(db: Session, request: TaskRequest) -> TaskResponse:
    try:
        new_task = Task(
            title=request.title,
            user_id=request.user_id,
        )
        db.add(new_task)
        db.commit()
        db.refresh(
            new_task
        )  # useful for getting database-generated values the ID of the new row.
        return new_task
    except IntegrityError as e:
        # Handle IntegrityError (UNIQUE constraint violation)
        db.rollback()
        print(f"Error creating user: {e}")
    finally:
        db.close()


def delete(db: Session, id: int) -> None:
    try:
        task = db.query(Task).filter(Task.id == id).first()
        if task:
            db.delete(task)
            db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()
