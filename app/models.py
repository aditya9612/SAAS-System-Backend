from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    role = Column(String(50))


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)
    gender = Column(String(20))
    phone = Column(String(20))
    address = Column(String(255))


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    specialization = Column(String(100))
    experience = Column(Integer)
    phone = Column(String(20))


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    appointment_date = Column(String(50))
    status = Column(String(50), default="Pending")


class Billing(Base):
    __tablename__ = "billing"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    amount = Column(Float)
    payment_status = Column(String(50), default="Pending")


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    report_name = Column(String(100))
    diagnosis = Column(String(255))
    prescription = Column(String(255))