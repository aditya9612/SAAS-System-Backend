from sqlalchemy.orm import Session
from .models import Student, Course
from .schemas import StudentCreate, CourseCreate


def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        email=student.email,
        password=student.password
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session):
    return db.query(Student).all()


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        course_name=course.course_name,
        faculty_name=course.faculty_name
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


def get_courses(db: Session):
    return db.query(Course).all()