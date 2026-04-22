from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def get_user(db: Session, user_id: int):
    """Bring user with id"""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """Bring user with email address"""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    """Creates new user and save to db"""

    fake_hashed_password = user.password + "_secret_hash"
    
  
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def update_user(db: Session, user_id: int, user_in: UserUpdate):
    """update user"""
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    
    update_data = user_in.model_dump(exclude_unset=True)
    
    if "password" in update_data:
        update_data["hashed_password"] = update_data.pop("password") + "_secret_hash"
        
    for field, value in update_data.items():
        setattr(db_user, field, value)
        
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    """delete user"""
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user