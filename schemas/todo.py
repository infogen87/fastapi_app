
from pydantic import BaseModel
from typing import Optional


class TodoBase(BaseModel):
    user_id: str
    title: str
    description: str
    is_completed: Optional[bool] = None 


class Todo(TodoBase):
    id: str


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None  