from db import Base, int32_pk, str_128, numeric_10_2
from sqlalchemy import  ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    __tablename__ = "book"
    __table_args__ = (
        CheckConstraint("amount > 0", name="check_amount_range"),
    )

    id: Mapped[int32_pk]
    title: Mapped[str_128]
    price: Mapped[numeric_10_2]
    amount: Mapped[int | None]

    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("ganre.id")) 
