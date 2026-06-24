import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_image(
    user_id,
    image_file,
    effect_name
):

    files = {
        "image": image_file
    }

    response = requests.post(
        f"{BASE_URL}/upload-image",
        params={
            "user_id": user_id,
            "effect_name": effect_name
        },
        files=files
    )

    return response.json()