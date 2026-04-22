from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine, Base
from app.models.user import User
from app.models.list import ShoppingList
from app.models.item import Item
from app.api.routers import users, lists, items

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(users.router)
app.include_router(lists.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} API is working!"}