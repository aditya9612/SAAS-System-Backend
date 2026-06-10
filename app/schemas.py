from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    email: str
    password: str


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    course_name: str
    faculty_name: str


class CourseResponse(BaseModel):
    id: int
    course_name: str
    faculty_name: str

    class Config:
        from_attributes = True