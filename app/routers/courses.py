from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post("/add",
             response_model=schemas.CourseResponse)
def add_course(
        course: schemas.CourseCreate,
        db: Session = Depends(get_db)
):
    return crud.create_course(db, course)


@router.get("/")
def get_courses(
        db: Session = Depends(get_db)
):
    return crud.get_courses(db)