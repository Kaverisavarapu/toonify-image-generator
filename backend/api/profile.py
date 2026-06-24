from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.models.user import User
from backend.services.image_service import (
    get_total_images
)
from backend.services.auth_service import (
    change_password_service
)
router = APIRouter()


@router.get("/profile/{user_id}")
def get_profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    return {
        "success": True,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
    }

@router.put("/profile/{user_id}")
def update_profile(
    user_id: int,
    username: str,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return {
            "success": False
        }

    user.username = username

    db.commit()

    db.refresh(user)

    return {
        "success": True,
        "message": "Profile updated"
    }
@router.get(
    "/profile-stats/{user_id}"
)
def profile_stats(
    user_id: int,
    db: Session = Depends(get_db)
):

    total_images = get_total_images(
        db,
        user_id
    )

    return {
        "total_images": total_images
    }

@router.put(
    "/change-password/{user_id}"
)
def change_password(
    user_id: int,
    old_password: str,
    new_password: str,
    db: Session = Depends(get_db)
):

    success, message = (
        change_password_service(
            db,
            user_id,
            old_password,
            new_password
        )
    )

    return {
        "success": success,
        "message": message
    }