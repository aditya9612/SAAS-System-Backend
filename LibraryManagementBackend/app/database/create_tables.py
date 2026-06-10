from app.database.database import Base, engine

from app.models.student_model import Student
from app.models.book_model import Book
from app.models.issue_model import IssuedBook
from app.models.fine_model import Fine

Base.metadata.create_all(bind=engine)

print("Tables created successfully")