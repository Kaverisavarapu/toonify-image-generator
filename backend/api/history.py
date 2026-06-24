from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.connection import get_db

from backend.services.image_service import (
    fetch_user_history
)

router = APIRouter()


@router.get("/history/{user_id}")
def history(
    user_id: int,
    db: Session = Depends(get_db)
):

    history = fetch_user_history(
        db,
        user_id
    )

    results = []

    for item in history:

        results.append(
            {
                "id": item.id,
                "effect_name": item.effect_name,
                "original_image": item.original_image,
                "generated_image": item.generated_image,
                "created_at": str(item.created_at)
            }
        )

    return results