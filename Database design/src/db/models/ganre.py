from db import Base, int32_pk, str_128
from sqlalchemy.orm import Mapped, mapped_column

class Ganre(Base):
    __tablename__ = "ganre"

    id: Mapped[int32_pk]
    name: Mapped[str_128]

