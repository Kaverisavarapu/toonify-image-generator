from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from pathlib import Path
import shutil
import uuid

from backend.database.connection import get_db
from backend.services.image_service import save_upload_record
from backend.services.image_service import (
    delete_history
)
from backend.services.effects_service import (
    generate_effect
)
router = APIRouter()

# Project root/backend path
BASE_DIR = Path(__file__).resolve().parent.parent

# Upload folder
UPLOAD_DIR = BASE_DIR / "uploads" / "originals"

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

@router.post("/upload-image")
async def upload_image(
    user_id: int,
    effect_name: str,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    print("1. Upload started")

    filename = f"{uuid.uuid4()}_{image.filename}"

    filepath = UPLOAD_DIR / filename

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    print("2. Image saved")

    history = save_upload_record(
        db=db,
        user_id=user_id,
        image_path=str(filepath),
        effect_name=effect_name
    )

    print("3. History saved")

    cartoon_dir = BASE_DIR / "uploads" / "cartoons"
    cartoon_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    print("4. Cartoon folder ready")

    cartoon_path = cartoon_dir / f"cartoon_{filename}"

    print("5. Before generate_effect")

    generate_effect(
        str(filepath),
        str(cartoon_path),
        effect_name
    )

    print("6. After generate_effect")

    from backend.services.image_service import update_cartoon_path

    update_cartoon_path(
        db,
        history.id,
        str(cartoon_path)
    )

    print("7. Database updated")

    return {
        "success": True,
        "history_id": history.id,
        "effect_name": effect_name,
        "original_image": f"https://toonify-image-generator-1.onrender.com/uploads/originals/{filename}",
        "cartoon_image": f"https://toonify-image-generator-1.onrender.com/uploads/cartoons/cartoon_{filename}"
    }

@router.delete(
    "/history/{history_id}"
)
async def remove_history(
    history_id: int,
    db: Session = Depends(get_db)
):

    success = delete_history(
        db,
        history_id
    )

    return {
        "success": success
    }