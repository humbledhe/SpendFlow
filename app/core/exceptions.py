class SpendFlowError(Exception):
    """Base-exception for all application specific exceptions"""


class NotFoundError(SpendFlowError):
    """Raised when the requested resource cannot be found"""


class CategoryNotFoundError(NotFoundError):
    """Raised when the requested category cannot be found"""


class ExpenseNotFoundError(NotFoundError):
    """Raised when the requested expense cannot be found"""
