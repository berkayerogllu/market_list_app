from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False) 
    quantity = Column(Float, default=1.0)      
    unit = Column(String, default="adet")         
    category = Column(String, default="Genel")      
    is_bought = Column(Boolean, default=False)      
    list_id = Column(Integer, ForeignKey("shopping_lists.id"))

    shopping_list = relationship("ShoppingList", back_populates="items")