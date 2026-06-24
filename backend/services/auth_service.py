from passlib.hash import bcrypt

from backend.repositories.user_repository import (
    get_user_by_email,
    create_user
)
from backend.repositories.user_repository import (
    update_password,
    get_user_by_email
)
from backend.models.user import User
def signup_service(db, username, email, password):

    if len(password) > 72:
        return False, "Password must be 72 characters or less"

    existing_user = get_user_by_email(db, email)

    if existing_user:
        return False, "Email already exists"

    hashed_password = bcrypt.hash(password[:72])

    user = create_user(
        db,
        {
            "username": username,
            "email": email,
            "password": hashed_password,
            "role": "user"
        }
    )

    return True, user
def login_service(db, email, password):

    user = get_user_by_email(db, email)

    if not user:
        return False, "User not found"

    if not bcrypt.verify(password[:72], user.password):
        return False, "Invalid password"

    return True, user


def change_password_service(
    db,
    user_id,
    old_password,
    new_password
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return False, "User not found"

    if not bcrypt.verify(
        old_password[:72],
        user.password
    ):
        return False, "Old password incorrect"

    new_hash = bcrypt.hash(
        new_password[:72]
    )

    update_password(
        db,
        user_id,
        new_hash
    )

    return True, "Password updated"