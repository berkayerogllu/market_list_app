from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.schemas.item import ItemResponse

class ShoppingListBase(BaseModel):
    title: str

class ShoppingListCreate(ShoppingListBase):
    pass

class ShoppingListResponse(ShoppingListBase):
    id: int
    user_id: int
    created_at: datetime
    items: List[ItemResponse] = [] 

    model_config = {"from_attributes": True}