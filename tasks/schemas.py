from pydantic import BaseModel


class Task(BaseModel):
    title: str
    id: int

    class Config:
        from_attributes = True


class TaskRequest(BaseModel):
    title: str
    user_id: int


class TaskResponse(BaseModel):
    title: str
    user_id: int
    id: int

    class Config:
        from_attributes = True
