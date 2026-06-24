import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"

def get_all_users():

    response = requests.get(
        f"{BASE_URL}/admin/users"
    )

    return response.json()