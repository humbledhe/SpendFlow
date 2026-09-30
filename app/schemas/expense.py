from pydantic import BaseModel, ConfigDict, Field, AwareDatetime

from uuid import UUID
from typing import Literal


class ExpenseBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    amount: int
    description: str


class ExpenseCreateModel(ExpenseBaseModel):
    category_id: UUID = Field(alias="categoryId")


class ExpenseUpdateModel(ExpenseBaseModel):
    pass


class ExpenseResponseModel(ExpenseBaseModel):
    expense_date: AwareDatetime = Field(alias="expenseDate")
    created_at: AwareDatetime = Field(alias="createdAt")
    updated_at: AwareDatetime = Field(alias="updatedAt")


class FilterParams(BaseModel):
    limit: int = Field(10, gt=0)
    order_by: Literal["amount", "expenseDate"] = "amount"
