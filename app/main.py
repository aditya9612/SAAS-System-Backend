from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

from .database import Base, engine, get_db
from .schemas import UserCreate, UserResponse
from .crud import create_user, get_users

from fastapi import HTTPException
from .models import User
from .auth import create_access_token

Base.metadata.create_all(bind=engine)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter



@app.post("/users")
@limiter.limit("5/minute")
def add_user(
    request: Request,
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


@app.get("/users")
def read_users(
    db: Session = Depends(get_db)
):
    return get_users(db)


@app.post("/login")
def login(email: str, password: str,
          db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid User"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }