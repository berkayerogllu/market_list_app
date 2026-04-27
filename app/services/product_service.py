from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate , ProductUpdate

def get_products(db: Session, category_id: int = None, search: str = None, skip: int = 0, limit: int = 100):
    """
    Bring products with filters
    """
    query = db.query(Product)
    
    if category_id:
        query = query.filter(Product.category_id == category_id)
        
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))
  
    return query.offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    """List one product"""
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product_in: ProductCreate):
    """Add new product to catalog"""
    db_product = Product(**product_in.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product_in: ProductUpdate):
    """Updates product details"""
    db_product = get_product(db, product_id)
    if not db_product:
        return None
        
    update_data = product_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)
        
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    """Deletes a product"""
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product