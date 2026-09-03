from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import users, expenses


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Expense Tracking API",
    description="A simple REST API for tracking personal expenses.",
    version="1.0.0"
)


app.include_router(users.router)
app.include_router(expenses.router)


@app.get("/")
def root():
    return {
        "message": "Expense Tracking API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }