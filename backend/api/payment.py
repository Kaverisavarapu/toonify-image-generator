from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.database.connection import get_db

from backend.services.payment_service import (
    fetch_user_payments
)

from backend.services.razorpay_service import (
    create_order
)

from backend.repositories.payment_repository import (
    create_payment
)

router = APIRouter()


@router.get("/payments/{user_id}")
async def get_payments(
    user_id: int,
    db: Session = Depends(get_db)
):

    payments = fetch_user_payments(
        db,
        user_id
    )

    return [
        {
            "id": p.id,
            "effect_name": p.effect_name,
            "amount": float(p.amount),
            "status": p.status,
            "created_at": str(p.created_at)
        }
        for p in payments
    ]


@router.post("/create-order")
async def create_payment_order(
    amount: int
):

    order = create_order(
        amount
    )

    return order


@router.post("/save-payment")
async def save_payment(
    user_id: int,
    effect_name: str,
    amount: float,
    payment_id: str,
    db: Session = Depends(get_db)
):

    payment = create_payment(
        db=db,
        user_id=user_id,
        effect_name=effect_name,
        amount=amount,
        status="success"
    )

    payment.payment_id = payment_id

    db.commit()

    return {
        "success": True
    }