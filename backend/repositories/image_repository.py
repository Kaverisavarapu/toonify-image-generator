from backend.models.image_history import ImageHistory


def save_image_history(
    db,
    user_id,
    effect_name,
    original_image,
    generated_image=""
):

    history = ImageHistory(
        user_id=user_id,
        effect_name=effect_name,
        original_image=original_image,
        generated_image=generated_image
    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return history


def update_generated_image(
    db,
    history_id,
    generated_image
):

    history = (
        db.query(ImageHistory)
        .filter(
            ImageHistory.id == history_id
        )
        .first()
    )

    if history:

        history.generated_image = generated_image

        db.commit()

        db.refresh(history)

    return history

def get_user_history(
    db,
    user_id
):

    return (
        db.query(ImageHistory)
        .filter(
            ImageHistory.user_id == user_id
        )
        .order_by(
            ImageHistory.id.desc()
        )
        .all()
    )

def delete_history_record(
    db,
    history_id
):

    history = (
        db.query(ImageHistory)
        .filter(
            ImageHistory.id == history_id
        )
        .first()
    )

    if history:

        db.delete(history)

        db.commit()

        return True

    return False

def get_user_total_images(
    db,
    user_id
):

    return (
        db.query(ImageHistory)
        .filter(
            ImageHistory.user_id == user_id
        )
        .count()
    )