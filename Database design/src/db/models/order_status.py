from db import Base, int32_pk, str_128
from sqlalchemy.orm import Mapped, mapped_column

class Order_status(Base):
    __tablename__ = "order_status"

    id: Mapped[int32_pk]
    step: Mapped[str_128]