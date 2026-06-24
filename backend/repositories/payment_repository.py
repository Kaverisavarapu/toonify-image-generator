from backend.models.payment import Payment



def create_payment(
    db,
    user_id,
    effect_name,
    amount,
    status
):

    payment = Payment(
        user_id=user_id,
        effect_name=effect_name,
        amount=amount,
        status=status
    )

    db.add(payment)

    db.commit()

    db.refresh(payment)

    return payment

def get_user_payments(
    db,
    user_id
):

    return (
        db.query(Payment)
        .filter(
            Payment.user_id == user_id
        )
        .order_by(
            Payment.created_at.desc()
        )
        .all()
    )