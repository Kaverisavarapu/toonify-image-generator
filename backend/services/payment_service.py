from backend.repositories.payment_repository import (
    create_payment
)

from backend.repositories.user_repository import (
    upgrade_user
)




from backend.repositories.payment_repository import (
    get_user_payments
)

def payment_history(
    db,
    user_id
):

    return get_user_payments(
        db,
        user_id
    )

from backend.repositories.payment_repository import (
    get_user_payments
)


def fetch_user_payments(
    db,
    user_id
):

    return get_user_payments(
        db,
        user_id
    )