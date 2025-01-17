from db import Base, int32_pk
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column


class Order_status_history(Base):
    __tablename__ = "order_status_history"
    __table_args__ = (
        CheckConstraint("date_beg < date_end", name='date_beg_less_than_date_end'),
        CheckConstraint("date_beg >= '2025-01-01'::date", name='date_beg_after_2025'),
    )

    id: Mapped[int32_pk]
    date_beg: Mapped[datetime] = mapped_column(DateTime)
    date_end: Mapped[datetime] = mapped_column(DateTime)

    purchase_id: Mapped[int] = mapped_column(ForeignKey("purchase.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("order_status.id"))