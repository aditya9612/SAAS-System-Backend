from fastapi import APIRouter

router = APIRouter(
    prefix="/marks",
    tags=["Marks"]
)

@router.post("/add")
def add_marks():
    return {"message": "Marks Added"}