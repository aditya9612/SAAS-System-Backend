from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.student_model import Student
from app.models.issue_model import IssuedBook

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register_student(
    name: str,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    try:
        student = Student(
            name=name,
            email=email,
            password=password
        )

        db.add(student)
        db.commit()
        db.refresh(student)

        return {
            "message": "Student Registered Successfully"
        }

    except Exception as e:
        print("ERROR:", e)
        db.rollback()
        return {"error": str(e)}

@router.get("/history/{id}")
def get_student_history(
    id: int,
    db: Session = Depends(get_db)
):
    history = db.query(IssuedBook).filter(
        IssuedBook.student_id == id
    ).all()

    return history