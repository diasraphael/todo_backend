from .models import Task
from sqlalchemy.orm.session import Session
from .schemas import TaskRequest, TaskResponse
from sqlalchemy.exc import IntegrityError

def create(db: Session, request: TaskRequest)-> TaskResponse:
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
