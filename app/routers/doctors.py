from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db
from app.models import Doctor
from app.schemas import DoctorCreate

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post("/add")
def add_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):

    new_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        experience=doctor.experience,
        phone=doctor.phone
    )

    db.add(new_doctor)
    db.commit()

    return {
        "message": "Doctor Added"
    }


@router.get("/")
def get_doctors(
    db: Session = Depends(get_db)
):
    return db.query(Doctor).all()