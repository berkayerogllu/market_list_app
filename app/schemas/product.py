from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    brand: Optional[str] = None
    image_url: Optional[str] = None
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    
    model_config = {"from_attributes": True}