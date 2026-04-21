from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    quantity: float = 1.0
    unit: str = "adet"
    category: str = "Genel"
    is_bought: bool = False

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    list_id: int

    model_config = {"from_attributes": True}