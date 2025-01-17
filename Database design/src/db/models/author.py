from db import Base, int32_pk, str_128
from sqlalchemy.orm import Mapped, mapped_column


class Author(Base):
    __tablename__ = "author"

    id: Mapped[int32_pk]
    name: Mapped[str_128] = mapped_column(nullable=False)




