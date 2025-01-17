from db import Base, int32_pk
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

class Purchase(Base):
    __tablename__ = "purchase"

    id: Mapped[int32_pk]
    description: Mapped[str] = mapped_column(String(512))

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
