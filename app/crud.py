from sqlalchemy.orm import Session

from app import models


def create_patient(
    db: Session,
    patient
):
    db_patient = models.Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        address=patient.address
    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient