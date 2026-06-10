from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.fine_model import FineReport

router = APIRouter(
    prefix="/fine",
    tags=["Fine Report"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/report")
def get_fine_report(
    db: Session = Depends(get_db)
):
    fines = db.query(FineReport).all()

    return fines