from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.book import Book
from app.models.issued_book import IssuedBook
from app.models.fine_report import FineReport

router = APIRouter(
    prefix="/books",
    tags=["Book Return"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/return")
def return_book(issue_id: int,
                db: Session = Depends(get_db)):

    issue = db.query(IssuedBook).filter(
        IssuedBook.id == issue_id
    ).first()

    if not issue:
        return {"error": "Issue record not found"}

    book = db.query(Book).filter(
        Book.id == issue.book_id
    ).first()

    book.quantity += 1

    fine = 0

    fine_report = FineReport(
        student_id=issue.student_id,
        fine_amount=fine
    )

    db.add(fine_report)

    db.commit()

    return {
        "message": "Book Returned Successfully",
        "fine": fine
    }
