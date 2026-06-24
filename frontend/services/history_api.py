import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"


def get_history(user_id):

    response = requests.get(
        f"{BASE_URL}/history/{user_id}"
    )

    return response.json()