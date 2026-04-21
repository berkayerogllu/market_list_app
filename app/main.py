from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine, Base

from app.models.user import User
from app.models.list import ShoppingList
from app.models.item import Item

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} API working! Tables ready."}