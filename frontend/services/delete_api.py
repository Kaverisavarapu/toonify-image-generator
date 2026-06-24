import requests

BASE_URL = "http://127.0.0.1:8000"

def delete_history_item(
    history_id
):

    response = requests.delete(
        f"{BASE_URL}/history/{history_id}"
    )

    return response.json()