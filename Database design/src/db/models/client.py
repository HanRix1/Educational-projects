from db import Base, int32_pk, str_128
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Client(Base):
    __tablename__ = "client"

    id: Mapped[int32_pk] 
    name: Mapped[str_128]
    email: Mapped[str_128]
    
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"), nullable=False)
