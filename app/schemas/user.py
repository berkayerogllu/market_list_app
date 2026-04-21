from pydantic import BaseModel
from typing import List
from app.schemas.list import ShoppingListResponse

class UserBase(BaseModel):
    email: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str 

class UserResponse(UserBase):
    id: int
    
    lists: List[ShoppingListResponse] = []

    model_config = {"from_attributes": True}