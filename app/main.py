from fastapi import FastAPI

from app.routes.category import router as category_router
from app.routes.expense import router as expense_router
from app.core.exceptions import NotFoundError
from app.core.exception_handlers import not_found_error

app = FastAPI()

app.add_exception_handler(NotFoundError, not_found_error)

app.include_router(category_router, prefix="/categories", tags=["Category"])
app.include_router(expense_router, prefix="/expenses", tags=["Expense"])
