from datetime import datetime
from pydantic import BaseModel, EmailStr


from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    age: int
    created_at: datetime = datetime.now()

    

class UserCreate(UserBase):
   pass


class User(BaseModel):
    id: str    


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
