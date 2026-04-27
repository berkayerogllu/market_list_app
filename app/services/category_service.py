from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate , CategoryUpdate

def get_categories(db: Session):
    """List all categories"""
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    """List one category"""
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, category_in: CategoryCreate):
    """Creates a new category"""
    db_category = Category(**category_in.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category_in: CategoryUpdate):
    """Updates category details"""
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    
    update_data = category_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_category, field, value)
        
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    """Deletes a category"""
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category