from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.services.auth_service import signup_service
from backend.services.auth_service import (
    signup_service,
    login_service
)
from backend.utils.security import create_access_token
router = APIRouter()


@router.post("/signup")
def signup(
    username: str,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    success, result = signup_service(
        db,
        username,
        email,
        password
    )

    if not success:
        return {
            "success": False,
            "message": result
        }

    return {
        "success": True,
        "message": "User created"
    }
@router.post("/login")
def login(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    success, result = login_service(
        db,
        email,
        password
    )

    if not success:
        return {
            "success": False,
            "message": result
        }

    token = create_access_token(
    {
        "user_id": result.id,
        "email": result.email,
        "role": result.role
    }
)

    return {
        "success": True,
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": result.id,
            "username": result.username,
            "email": result.email,
            "role": result.role
        }
    }