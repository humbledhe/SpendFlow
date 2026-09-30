from sqlalchemy import Uuid, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from uuid import UUID, uuid7
from datetime import datetime

from .base import Base


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid7, index=True)

    category_id: Mapped[UUID] = mapped_column("categoryId", ForeignKey("categories.id"))

    amount: Mapped[int]

    description: Mapped[str]

    expense_date: Mapped[datetime] = mapped_column(
        "expenseDate", DateTime(timezone=True), server_default=func.now()
    )

    created_at: Mapped[datetime] = mapped_column(
        "createdAt", DateTime(timezone=True), server_default=func.now()
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        "updatedAt", DateTime(timezone=True), onupdate=func.now()
    )
