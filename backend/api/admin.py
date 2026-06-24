from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.models.user import User
from backend.models.image_history import ImageHistory
from backend.services.admin_service import (
    fetch_all_users
)
router = APIRouter()


@router.get("/admin/stats")
def admin_stats(
    db: Session = Depends(get_db)
):

    total_users = (
        db.query(User)
        .count()
    )

    total_images = (
        db.query(ImageHistory)
        .count()
    )

    return {
        "total_users": total_users,
        "total_images": total_images
    }

@router.get("/admin/users")
def admin_users(
    db: Session = Depends(get_db)
):

    users = fetch_all_users(db)

    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
        for user in users
    ]