from sqlalchemy import select, update, delete, desc
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreateModel, ExpenseUpdateModel, FilterParams


class ExpenseServices:
    async def get_expenses(self, session: AsyncSession, filter_query: FilterParams):
        order_by = desc(filter_query.order_by)
        limit = filter_query.limit

        stmt = select(Expense).order_by(order_by).limit(limit)
        stmt = select(Expense).order_by(order_by).limit(limit)
        stmt = select(Expense).order_by(order_by).limit(limit)
        result = await session.execute(stmt)
        expenses = result.scalars().all()

        return expenses

    async def get_expense(self, expense_uid: UUID, session: AsyncSession):
        stmt = select(Expense).where(Expense.id == expense_uid)
        result = await session.execute(stmt)
        expense = result.scalar()

        return expense

    async def create_expense(self, expense: ExpenseCreateModel, session: AsyncSession):
        new_expense = Expense(**expense.model_dump())

        session.add(new_expense)
        await session.commit()
        await session.refresh(new_expense)

        return new_expense

    async def update_expense(
        self, expense_uid: UUID, new_expense: ExpenseUpdateModel, session: AsyncSession
    ):
        stmt = (
            update(Expense)
            .where(Expense.id == expense_uid)
            .values(**new_expense.model_dump())
            .returning(Expense)
        )
        result = await session.execute(stmt)
        updated_expense = result.scalars().first()

        await session.commit()

        return updated_expense

    async def delete_expense(self, expense_uid: UUID, session: AsyncSession):
        stmt = delete(Expense).where(Expense.id == expense_uid)
        result = await session.execute(stmt)

        await session.commit
