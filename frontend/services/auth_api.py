import requests

BASE_URL = "https://toonify-image-generator-1.onrender.com"


def login_user(email, password):

    try:

        response = requests.post(
            f"{BASE_URL}/login",
            params={
                "email": email,
                "password": password
            }
        )

        print("LOGIN STATUS:", response.status_code)
        print("LOGIN RESPONSE:", response.text)

        return response.json()

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }


def signup_user(username, email, password):

    try:

        response = requests.post(
            f"{BASE_URL}/signup",
            params={
                "username": username,
                "email": email,
                "password": password
            }
        )

        print("SIGNUP STATUS:", response.status_code)
        print("SIGNUP RESPONSE:", response.text)

        return response.json()

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }