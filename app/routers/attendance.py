from fastapi import APIRouter

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.post("/mark")
def mark_attendance():
    return {"message": "Attendance Marked"}

@router.get("/{student_id}")
def get_attendance(student_id: int) -> dict[str, int]:
    return {"student_id": student_id}