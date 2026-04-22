from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate

def get_items_by_list(db: Session, list_id: int):
    """get all items in the specific list"""
    return db.query(Item).filter(Item.list_id == list_id).all()

def create_item(db: Session, item_in: ItemCreate, list_id: int):
    """add an item to specific list"""
    db_item = Item(
        name=item_in.name,
        quantity=item_in.quantity,
        unit=item_in.unit,
        category=item_in.category,
        is_bought=item_in.is_bought,
        list_id=list_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item_status(db: Session, item_id: int, is_bought: bool):
    """is bought so it determines the item is bought or not"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db_item.is_bought = is_bought
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    """delete item"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item