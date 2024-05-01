from datetime import datetime
from pydantic import BaseModel, Field

from util.formatter import to_camel


class TaskEntry(BaseModel):
    id: int
    status: bool
    task_id: int
    task_date: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# from frontend we will be getting userId instead of user_id
class TaskEntryRequest(BaseModel):
    status: bool
    task_id: int = Field(..., alias="taskId")
    task_date: datetime = Field(..., alias="taskDate")


# if we want a model to be shown or passed to the user that model needs to be configured with Config class
class TaskEntryResponse(BaseModel):
    id: int
    status: bool
    task_id: int
    task_date: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        alias_generator = to_camel
        populate_by_name = True
