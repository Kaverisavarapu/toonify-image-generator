import requests

BASE_URL = "http://127.0.0.1:8000"

def get_all_users():

    response = requests.get(
        f"{BASE_URL}/admin/users"
    )

    return response.json()