from sqlalchemy import Column, Integer, Date
from app.database.database import Base

class IssuedBook(Base):
    __tablename__ = "issued_books"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    book_id = Column(Integer)
    issue_date = Column(Date)
    return_date = Column(Date)