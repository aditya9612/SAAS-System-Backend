from app.models.student_model import Student
from app.utils.auth import hash_password

def register_student(data, db):

    student = Student(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(student)
    db.commit()

    return {"message":"Student Registered"}