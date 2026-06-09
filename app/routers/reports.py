from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

# Add Report
@router.post("/add")
def add_report(
    report: schemas.ReportCreate,
    db: Session = Depends(get_db)
):
    new_report = models.Report(
        patient_id=report.patient_id,
        report_name=report.report_name,
        diagnosis=report.diagnosis,
        prescription=report.prescription
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return {
        "message": "Report Added Successfully",
        "id": new_report.id
    }


# Get Reports By Patient ID
@router.get("/patient/{id}")
def get_patient_reports(
    id: int,
    db: Session = Depends(get_db)
):
    reports = db.query(models.Report).filter(
        models.Report.patient_id == id
    ).all()

    if not reports:
        raise HTTPException(
            status_code=404,
            detail="No reports found for this patient"
        )

    return reports
