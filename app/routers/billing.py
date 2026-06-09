from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)

@router.post("/add")
def add_billing(
    bill: schemas.BillingCreate,
    db: Session = Depends(get_db)
):
    new_bill = models.Billing(
        patient_id=bill.patient_id,
        amount=bill.amount,
        payment_status=bill.payment_status
    )

    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)

    return {
        "message": "Bill Added Successfully",
        "id": new_bill.id
    }