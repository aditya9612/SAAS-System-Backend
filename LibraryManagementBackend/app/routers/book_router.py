from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.book_model import Book

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add")
def add_book(db: Session = Depends(get_db)):

    book = Book(
        title="Python",
        author="John",
        quantity=10,
        available=10
    )

    db.add(book)
    db.commit()

    return {"message": "Book Added Successfully"}


@router.get("/")
def get_books(db: Session = Depends(get_db)):

    books = db.query(Book).all()

    return books


@router.put("/update/{id}")
def update_book(id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.id == id).first()

    if not book:
        return {"error": "Book not found"}

    book.title = "Updated Python"

    db.commit()

    return {"message": "Book Updated"}


@router.delete("/delete/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.id == id).first()

    if not book:
        return {"error": "Book not found"}

    db.delete(book)
    db.commit()

    return {"message": "Book Deleted"}