from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db
from app.schemas import UserCreate
from app.models import User
from app.auth import hash_password
from app.schemas import UserLogin
from app.auth import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(
            user.password
        ),
        role=user.role
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User Registered"
    }

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return {
            "message": "User not found"
        }

    if not verify_password(
        user.password,
        db_user.password
    ):
        return {
            "message": "Invalid password"
        }

    return {
        "message": "Login Successful"
    }