import os
import razorpay

from dotenv import load_dotenv

load_dotenv()

RAZORPAY_KEY = os.getenv(
    "RAZORPAY_KEY"
)

RAZORPAY_SECRET = os.getenv(
    "RAZORPAY_SECRET"
)

client = razorpay.Client(
    auth=(
        RAZORPAY_KEY,
        RAZORPAY_SECRET
    )
)


def create_order(
    amount
):

    return client.order.create(
        {
            "amount": amount * 100,
            "currency": "INR",
            "payment_capture": 1
        }
    )