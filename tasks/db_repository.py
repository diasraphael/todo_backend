from .models import Task
from sqlalchemy.orm.session import Session
from .schemas import TaskRequest, TaskResponse
from sqlalchemy.exc import IntegrityError
from typing import List

def get(db: Session) -> List[TaskResponse]:
    tasks = db.query(Task).all()
    return tasks

def create(db: Session, request: TaskRequest) -> TaskResponse:
    try:
        new_task = Task(
            title=request.title,
            user_id=request.user_id,
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)  # this allows to give us an taskId
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
        print("I am printing", task, id)
        if task:
            db.delete(task)
            db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()
