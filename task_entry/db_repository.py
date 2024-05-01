from datetime import datetime
from task_entry.models import TaskEntry
from sqlalchemy.orm.session import Session
from .schemas import TaskEntryRequest, TaskEntryResponse
from sqlalchemy.exc import IntegrityError


def create_task_entry(db: Session, request: TaskEntryRequest) -> TaskEntryResponse:
    try:
        new_task_entry = TaskEntry(
            task_id=request.task_id,
            status=request.status,
            task_date=request.task_date,
            updated_at=datetime.utcnow(),
        )
        db.add(new_task_entry)
        db.commit()
        db.refresh(
            new_task_entry
        )  # useful for getting database-generated values the ID of the new row.
        return new_task_entry
    except IntegrityError as e:
        # Handle IntegrityError (UNIQUE constraint violation)
        db.rollback()
        print(f"Error creating user: {e}")
    finally:
        db.close()
