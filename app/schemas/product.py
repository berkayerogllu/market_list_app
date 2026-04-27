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

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    image_url: Optional[str] = None
    category_id: Optional[int] = None   
    
    model_config = {"from_attributes": True}