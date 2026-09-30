from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated
from uuid import UUID

from app.services.expense import ExpenseServices
from app.core.dependencies import get_async_db
from app.core.exceptions import ExpenseNotFoundError
from app.schemas.expense import ExpenseCreateModel, ExpenseUpdateModel, FilterParams

router = APIRouter()
expense_services = ExpenseServices()

DbDependency = Annotated[AsyncSession, Depends(get_async_db)]
FilterQuery = Annotated[FilterParams, Query()]


@router.get("/")
async def get_expenses(session: DbDependency, filter_query: FilterQuery):
    expenses = await expense_services.get_expenses(session, filter_query)

    return expenses


@router.get("/{expense_uid}")
async def get_expense(expense_uid: UUID, session: DbDependency):
    expense = await expense_services.get_expense(expense_uid, session)

    return expense


@router.post("/")
async def create_expense(expense: ExpenseCreateModel, session: DbDependency):
    new_expense = await expense_services.create_expense(expense, session)

    return new_expense


@router.put("/{expense_uid}")
async def update_expense(
    expense_uid: UUID, new_expense: ExpenseUpdateModel, session: DbDependency
):
    expense = await expense_services.get_expense(expense_uid, session)

    if not expense:
        raise ExpenseNotFoundError("The requested expense cannot be found")

    updated_expense = await expense_services.update_expense(
        expense_uid, new_expense, session
    )

    return updated_expense


@router.delete("/{expense_uid}")
async def delete_expense(expense_uid: UUID, session: DbDependency):
    expense = await expense_services.get_expense(expense_uid, session)

    if not expense:
        raise ExpenseNotFoundError("The requested expense cannot be found")

    await expense_services.delete_expense(expense_uid, session)

    return {"message": "Expense deleted successfully"}
