from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    icon: Optional[str] = None
    color_code: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    model_config = {"from_attributes": True}