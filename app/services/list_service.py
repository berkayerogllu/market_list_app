from sqlalchemy.orm import Session
from app.models.list import ShoppingList
from app.schemas.list import ShoppingListCreate

def get_list(db: Session, list_id: int):
    """get list by list id"""
    return db.query(ShoppingList).filter(ShoppingList.id == list_id).first()

def get_lists_by_user(db: Session, user_id: int):
    """get all lists of an user"""
    return db.query(ShoppingList).filter(ShoppingList.user_id == user_id).all()

def create_user_list(db: Session, list_in: ShoppingListCreate, user_id: int):
    """create a new list for user"""
    db_list = ShoppingList(title=list_in.title, user_id=user_id)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

def delete_list(db: Session, list_id: int):
    """delete a list"""
    db_list = get_list(db, list_id=list_id)
    if db_list:
        db.delete(db_list)
        db.commit()
    return db_list