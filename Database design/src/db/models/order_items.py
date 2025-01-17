from db import Base, int32_pk, str_128
from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Order_items(Base):
    __tablename__ = "order_items"
    __table_args__ = (
        CheckConstraint("amount > 0", name="check_Order_items.amount_gt_zero"),
    )

    id: Mapped[int32_pk]
    amount: Mapped[int]

    purchase_id: Mapped[int] = mapped_column(ForeignKey("purchase.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"))