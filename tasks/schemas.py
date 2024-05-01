from pydantic import BaseModel, Field

from util.formatter import to_camel


class Task(BaseModel):
    title: str
    id: int

    class Config:
        from_attributes = True


class TaskRequest(BaseModel):
    title: str
    user_id: int = Field(..., alias="userId")


class TaskResponse(BaseModel):
    title: str
    user_id: int = Field(..., alias="userId")
    id: int

    class Config:
        from_attributes = True
        alias_generator = to_camel
        populate_by_name = True

        # we are using this config to convert the snake_case to camelCase
