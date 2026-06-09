from fastapi import FastAPI
from app.database import engine
from app import models

from app.routers import (
    auth,
    patients,
    doctors,
    appointment,
    billing,
    reports
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointment.router)
app.include_router(billing.router)
app.include_router(reports.router)

@app.get("/")
def home():
    return {"message": "Hospital API Running"}