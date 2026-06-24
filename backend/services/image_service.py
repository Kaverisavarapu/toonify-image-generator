from backend.repositories.image_repository import (
    save_image_history
)
from backend.repositories.image_repository import (
    update_generated_image
)
from backend.repositories.image_repository import (
    get_user_history
)
def save_upload_record(
    db,
    user_id,
    image_path,
    effect_name
):

    return save_image_history(
        db=db,
        user_id=user_id,
        effect_name=effect_name,
        original_image=image_path,
        generated_image=""
    )

def update_cartoon_path(
    db,
    history_id,
    cartoon_path
):

    return update_generated_image(
        db,
        history_id,
        cartoon_path
    )

def fetch_user_history(
    db,
    user_id
):

    return get_user_history(
        db,
        user_id
    )
from backend.repositories.image_repository import (
    delete_history_record
)

def delete_history(
    db,
    history_id
):

    return delete_history_record(
        db,
        history_id
    )

from backend.repositories.image_repository import (
    get_user_total_images
)

def get_total_images(
    db,
    user_id
):

    return get_user_total_images(
        db,
        user_id
    )