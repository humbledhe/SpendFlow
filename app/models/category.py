from sqlalchemy import Uuid, DateTime, func, String
from sqlalchemy.orm import Mapped, mapped_column

from uuid import UUID, uuid7
from datetime import datetime, timezone

from .base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid7, index=True)

    name: Mapped[str] = mapped_column(String(30), index=True)

    description: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(
        "createdAt", DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        "updatedAt", DateTime(timezone=True), onupdate=func.now()
    )
