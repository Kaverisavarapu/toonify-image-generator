import requests

BASE_URL = "http://127.0.0.1:8000"


def get_history(user_id):

    response = requests.get(
        f"{BASE_URL}/history/{user_id}"
    )

    return response.json()