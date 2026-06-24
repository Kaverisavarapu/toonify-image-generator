import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"

def delete_history_item(
    history_id
):

    response = requests.delete(
        f"{BASE_URL}/history/{history_id}"
    )

    return response.json()