from fastapi import FastAPI

from app.database import engine, Base

from app.routers import (
    students,
    courses,
    enrollment,
    attendance,
    marks,
    results,
    dashboard
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Course Management System"
)

app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollment.router)
app.include_router(attendance.router)
app.include_router(marks.router)
app.include_router(results.router)
app.include_router(dashboard.router)


@app.get("/")
def home():
    return {
        "message": "Student Course Management System API"
    }