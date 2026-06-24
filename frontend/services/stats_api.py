import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"

def get_profile_stats(
    user_id
):

    response = requests.get(
        f"{BASE_URL}/profile-stats/{user_id}"
    )

    return response.json()