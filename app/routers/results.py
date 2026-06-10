from fastapi import APIRouter

router = APIRouter(
    prefix="/results",
    tags=["Results"]
)

@router.get("/{student_id}")
def get_result(student_id: int) -> dict[str, int | str]:
    return {
        "student_id": student_id,
        "grade": "A"
    }