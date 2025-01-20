from db import Base, uuid_pk, str_128, str_256
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime


class SpimexTradingResults(Base):
    __tablename__ = "spimex_trading_results"

    id: Mapped[uuid_pk]
    exchange_product_id: Mapped[str_128]
    exchange_product_name: Mapped[str_256]
    oil_id: Mapped[str_128]
    delivery_basis_id: Mapped[str_128]
    delivery_basis_name: Mapped[str_128]
    delivery_type_id: Mapped[str_128]
    volume: Mapped[int]
    total: Mapped[int]
    count: Mapped[int]
    date: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)
