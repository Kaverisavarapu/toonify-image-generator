from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from backend.database.connection import Base


class Payment(Base):

    __tablename__ = "payments"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer
    )

    effect_name = Column(
        String(50)
    )

    amount = Column(
        Numeric(10, 2)
    )

    payment_id = Column(
        String(255)
    )

    status = Column(
        String(30)
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )