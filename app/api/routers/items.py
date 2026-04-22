from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.item import ItemCreate, ItemResponse
from app.services import item_service

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(list_id: int, item_in: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db=db, item_in=item_in, list_id=list_id)

@router.get("/list/{list_id}", response_model=List[ItemResponse])
def read_items_by_list(list_id: int, db: Session = Depends(get_db)):
    return item_service.get_items_by_list(db=db, list_id=list_id)

@router.patch("/{item_id}/status", response_model=ItemResponse)
def update_item_status(item_id: int, is_bought: bool, db: Session = Depends(get_db)):
    db_item = item_service.update_item_status(db=db, item_id=item_id, is_bought=is_bought)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item could not find")
    return db_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_service.delete_item(db=db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item could not find")
    return None