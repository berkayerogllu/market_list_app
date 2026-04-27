from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False) 
    brand = Column(String, nullable=True)            
    image_url = Column(String, nullable=True)    
    

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")