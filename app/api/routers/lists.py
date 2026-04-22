from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.list import ShoppingListCreate, ShoppingListResponse
from app.services import list_service

router = APIRouter(
    prefix="/lists",
    tags=["Lists"]
)

@router.post("/", response_model=ShoppingListResponse, status_code=status.HTTP_201_CREATED)
def create_list(user_id: int, list_in: ShoppingListCreate, db: Session = Depends(get_db)):
    return list_service.create_user_list(db=db, list_in=list_in, user_id=user_id)

@router.get("/user/{user_id}", response_model=List[ShoppingListResponse])
def read_lists_by_user(user_id: int, db: Session = Depends(get_db)):
    return list_service.get_lists_by_user(db=db, user_id=user_id)

@router.get("/{list_id}", response_model=ShoppingListResponse)
def read_list(list_id: int, db: Session = Depends(get_db)):
    db_list = list_service.get_list(db=db, list_id=list_id)
    if not db_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="List could not find")
    return db_list

@router.delete("/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_list(list_id: int, db: Session = Depends(get_db)):
    db_list = list_service.delete_list(db=db, list_id=list_id)
    if not db_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="List could not find")
    return None