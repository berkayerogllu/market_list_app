from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services import product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db=db, product_in=product_in)

@router.get("/", response_model=List[ProductResponse])
def read_products(
    db: Session = Depends(get_db),
    category_id: Optional[int] = Query(None, description="category id of the product which want to filter"),
    search: Optional[str] = Query(None, description="word to search in product name"),
    skip: int = Query(0, description="pagination product size"),
    limit: int = Query(100, description="max product size to bring")
):
    return product_service.get_products(
        db=db, category_id=category_id, search=search, skip=skip, limit=limit
    )

@router.get("/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.get_product(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product could not find")
    return db_product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)):
    db_product = product_service.update_product(db=db, product_id=product_id, product_in=product_in)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product could not find")
    return db_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_service.delete_product(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product could not find")
    return None