from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)

# Add Appointment
@router.post("/add")
def add_appointment(
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):
    new_appointment = models.Appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        appointment_date=appointment.appointment_date,
        status=appointment.status
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return {
        "message": "Appointment Added Successfully",
        "id": new_appointment.id
    }


# Get All Appointments
@router.get("/")
def get_appointments(
    db: Session = Depends(get_db)
):
    appointments = db.query(
        models.Appointment
    ).all()

    return appointments


# Update Appointment
@router.put("/update/{id}")
def update_appointment(
    id: int,
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(
        models.Appointment
    ).filter(
        models.Appointment.id == id
    ).first()

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Appointment Not Found"
        )

    existing.patient_id = appointment.patient_id
    existing.doctor_id = appointment.doctor_id
    existing.appointment_date = appointment.appointment_date
    existing.status = appointment.status

    db.commit()

    return {
        "message": "Appointment Updated Successfully"
    }


# Delete Appointment
@router.delete("/delete/{id}")
def delete_appointment(
    id: int,
    db: Session = Depends(get_db)
):
    appointment = db.query(
        models.Appointment
    ).filter(
        models.Appointment.id == id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment Not Found"
        )

    db.delete(appointment)
    db.commit()

    return {
        "message": "Appointment Deleted Successfully"
    }