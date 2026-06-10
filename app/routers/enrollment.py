from fastapi import APIRouter

router = APIRouter(
    prefix="/enrollment",
    tags=["Enrollment"]
)

@router.post("/create")
def create_enrollment():
    return {"message": "Enrollment Created"}