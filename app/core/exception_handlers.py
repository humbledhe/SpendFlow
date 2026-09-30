from fastapi import Request, status
from fastapi.responses import JSONResponse

from .exceptions import NotFoundError


def not_found_error(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": str(exc)}
    )
