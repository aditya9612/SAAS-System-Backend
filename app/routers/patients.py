from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Patient
from app.schemas import PatientCreate

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/add")
def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address
    )

    db.add(new_patient)
    db.commit()

    return {
        "message": "Patient Added"
    }


@router.get("/")
def get_patients(
    db: Session = Depends(get_db)
):
    return db.query(Patient).all()