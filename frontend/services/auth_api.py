import requests

BASE_URL = "http://127.0.0.1:8000"


def login_user(email, password):

    response = requests.post(
        f"{BASE_URL}/login",
        params={
            "email": email,
            "password": password
        }
    )

    return response.json()


def signup_user(username, email, password):

    response = requests.post(
        f"{BASE_URL}/signup",
        params={
            "username": username,
            "email": email,
            "password": password
        }
    )

    return response.json()