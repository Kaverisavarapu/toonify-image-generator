import requests

BASE_URL = "http://127.0.0.1:8000"


def make_payment(
    user_id,
    effect_name,
    amount
):

    response = requests.post(
        f"{BASE_URL}/pay",
        params={
            "user_id": user_id,
            "effect_name": effect_name,
            "amount": amount
        }
    )

    return response.json()


def get_payments(
    user_id
):

    response = requests.get(
        f"{BASE_URL}/payments/{user_id}"
    )

    return response.json()


def create_order(
    amount
):

    response = requests.post(
        f"{BASE_URL}/create-order",
        params={
            "amount": amount
        }
    )

    return response.json()

def save_payment(
    user_id,
    effect_name,
    amount,
    payment_id
):

    response = requests.post(
        f"{BASE_URL}/save-payment",
        params={
            "user_id": user_id,
            "effect_name": effect_name,
            "amount": amount,
            "payment_id": payment_id
        }
    )

    return response.json()