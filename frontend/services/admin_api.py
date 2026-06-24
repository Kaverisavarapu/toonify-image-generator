import requests

BASE_URL = "http://127.0.0.1:8000"

def get_admin_stats():
    response = requests.get(
        f"{BASE_URL}/admin/stats"
    )
    return response.json()