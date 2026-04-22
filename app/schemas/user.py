from pydantic import BaseModel
from typing import List, Optional  # Optional eklendi
from app.schemas.list import ShoppingListResponse

class UserBase(BaseModel):
    email: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str
    
class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    lists: List[ShoppingListResponse] = []
    model_config = {"from_attributes": True}