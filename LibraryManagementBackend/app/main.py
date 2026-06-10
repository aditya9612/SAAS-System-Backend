from fastapi import FastAPI

from app.database.database import Base, engine

from app.models.student_model import Student
from app.models.book_model import Book
from app.models.issue_model import IssuedBook
from app.models.fine_model import FineReport

Base.metadata.create_all(bind=engine)

from app.routers.student_router import router as student_router
from app.routers.book_router import router as book_router
from app.routers.issue_router import router as issue_router
from app.routers.fine_router import router as fine_router

app = FastAPI(
    title="Library Management System"
)

app.include_router(student_router)
app.include_router(book_router)
app.include_router(issue_router)
app.include_router(fine_router)

@app.get("/")
def home():
    return {
        "message": "Library Management System API Running"
    }