from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlite.database import Base
from datetime import datetime


class TaskEntry(Base):
    __tablename__ = "task_entries"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    status = Column(Boolean, default=False)
    task_date = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now)

    task = relationship(
        "Task",
    )
