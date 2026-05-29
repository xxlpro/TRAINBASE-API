from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import AppError
from app.schemas.error import ErrorDetail, ErrorResponse


async def app_error_handler(
    _request: Request,
    exc: AppError,
) -> JSONResponse:
    error_response = ErrorResponse(
        error=ErrorDetail(
            code=exc.code,
            message=exc.message,
        )
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump(),
    )