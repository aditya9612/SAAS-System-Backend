from .models import User

def create_user(db, user_data):
    db_user = User(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db):
    return db.query(User).all()