from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")
    task_entries = relationship(
        "TaskEntry", back_populates="task", cascade="all, delete-orphan"
    )
