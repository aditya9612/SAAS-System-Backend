from app.models.book import Book
from app.models.student import Student
from app.models.issued_book import IssuedBook

def issue_book(db, student_id, book_id):

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
        return {"error": "Book unavailable"}

    issue = IssuedBook(
        student_id=student_id,
        book_id=book_id
    )

    db.add(issue)

    book.quantity -= 1

    db.commit()

    return {"message": "Book Issued"}