import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"

def get_admin_stats():
    response = requests.get(
        f"{BASE_URL}/admin/stats"
    )
    return response.json()