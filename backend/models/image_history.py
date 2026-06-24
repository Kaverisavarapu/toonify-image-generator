from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from backend.database.connection import Base


class ImageHistory(Base):

    __tablename__ = "image_history"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(Integer)

    effect_name = Column(String)

    original_image = Column(String)

    generated_image = Column(String)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )