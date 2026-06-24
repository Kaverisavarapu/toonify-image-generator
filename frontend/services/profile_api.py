import requests
import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"


def get_profile(user_id):

    response = requests.get(
        f"{BASE_URL}/profile/{user_id}"
    )

    return response.json()


def update_profile(
    user_id,
    username
):

    response = requests.put(
        f"{BASE_URL}/profile/{user_id}",
        params={
            "username": username
        }
    )

    return response.json()


def upgrade_to_premium(
    user_id
):

    response = requests.post(
        f"{BASE_URL}/premium/{user_id}"
    )

    return response.json()