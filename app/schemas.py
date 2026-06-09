from pydantic import BaseModel


# User login 

class UserLogin(BaseModel):
    email: str
    password: str


# User

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str


class UserLogin(BaseModel):
    email: str
    password: str


# Patient

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    address: str


# Doctor

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    experience: int
    phone: str


# Appointment

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: str
    status: str

# Billing

class BillingCreate(BaseModel):
    patient_id: int
    amount: float
    payment_status: str

# Report

class ReportCreate(BaseModel):
    patient_id: int
    report_name: str
    diagnosis: str
    prescription: str