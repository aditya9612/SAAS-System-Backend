from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/stats")
def dashboard_stats() -> dict[str, int]:
    return {
        "total_students": 100,
        "total_courses": 20,
        "total_enrollments": 50
    }