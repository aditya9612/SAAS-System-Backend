from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.student_model import Student
from app.models.book_model import Book
from app.models.issue_model import IssuedBook

router = APIRouter(
    prefix="/books",
    tags=["Book Issue"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/issue")
def issue_book(
    student_id: int,
    book_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return {"error": "Student not found"}

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:
        return {"error": "Book not found"}

    if book.quantity <= 0:
        return {"error": "Book not available"}

    issue = IssuedBook(
        student_id=student_id,
        book_id=book_id
    )

    db.add(issue)

    book.quantity -= 1

    db.commit()

    return {"message": "Book Issued Successfully"}