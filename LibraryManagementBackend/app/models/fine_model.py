from sqlalchemy import Column, Integer, Float
from app.database.database import Base

class FineReport(Base):
    __tablename__ = "fine_reports"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    fine_amount = Column(Float)