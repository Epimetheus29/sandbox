from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class SortHistory(Base):
    __tablename__ = "sort_history"

    id: Mapped[int] = mapped_column(primary_key=True)

    algorithm: Mapped[str] = mapped_column(String(50))

    input_data: Mapped[str]

    output_data: Mapped[str]