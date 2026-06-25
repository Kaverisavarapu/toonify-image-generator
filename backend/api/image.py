from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from pathlib import Path
import shutil
import uuid
import traceback

from backend.database.connection import get_db
from backend.services.image_service import (
    save_upload_record,
    delete_history,
    update_cartoon_path
)
from backend.services.effects_service import generate_effect

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads" / "originals"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload-image")
async def upload_image(
    user_id: int,
    effect_name: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:

        print("===== UPLOAD START =====")

        filename = f"{uuid.uuid4()}_{image.filename}"
        print("Filename:", filename)

        filepath = UPLOAD_DIR / filename

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        print("Image saved:", filepath)

        history = save_upload_record(
            db=db,
            user_id=user_id,
            image_path=str(filepath),
            effect_name=effect_name
        )

        print("History saved:", history.id)

        cartoon_dir = BASE_DIR / "uploads" / "cartoons"
        cartoon_dir.mkdir(parents=True, exist_ok=True)

        print("Cartoon directory:", cartoon_dir)

        cartoon_path = cartoon_dir / f"cartoon_{filename}"

        print("Generating effect:", effect_name)

        generate_effect(
            str(filepath),
            str(cartoon_path),
            effect_name
        )

        print("Cartoon generated:", cartoon_path)

        update_cartoon_path(
            db,
            history.id,
            str(cartoon_path)
        )

        print("Database updated")

        return {
            "success": True,
            "history_id": history.id,
            "effect_name": effect_name,
            "original_image": f"https://toonify-image-generator-1.onrender.com/uploads/originals/{filename}",
            "cartoon_image": f"https://toonify-image-generator-1.onrender.com/uploads/cartoons/cartoon_{filename}"
        }

    except Exception as e:

        print("========== ERROR ==========")
        traceback.print_exc()
        print("===========================")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete("/history/{history_id}")
async def remove_history(
    history_id: int,
    db: Session = Depends(get_db)
):
    success = delete_history(db, history_id)

    return {
        "success": success
    }