from sqlalchemy.orm import Session
from backend.models.user import User


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_data: dict):
    user = User(**user_data)

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

def upgrade_user(
    db,
    user_id
):

    user = (
        db.query(User)
        .filter(
            User.id == user_id
        )
        .first()
    )

    if user:

        user.role = "premium"

        db.commit()

        db.refresh(user)

    return user


def update_password(
    db,
    user_id,
    hashed_password
):

    user = (
        db.query(User)
        .filter(
            User.id == user_id
        )
        .first()
    )

    if user:

        user.password = hashed_password

        db.commit()

        db.refresh(user)

    return user


def get_all_users(db):

    return db.query(User).all()