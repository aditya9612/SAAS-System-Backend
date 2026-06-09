from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db


def get_database():
    db = next(get_db())
    return db