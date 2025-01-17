from db import Base, int32_pk, str_128
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

class City(Base):
    __tablename__ = "city"
    __table_args__ = (
        CheckConstraint("days_delivery > 0", name="check_days_delivery_range"),
    )

    id: Mapped[int32_pk]
    name: Mapped[str_128]
    days_delivery: Mapped[int]
    
