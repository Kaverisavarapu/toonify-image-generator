import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"

def change_password(
    user_id,
    old_password,
    new_password
):

    response = requests.put(
        f"{BASE_URL}/change-password/{user_id}",
        params={
            "old_password": old_password,
            "new_password": new_password
        }
    )

    return response.json()