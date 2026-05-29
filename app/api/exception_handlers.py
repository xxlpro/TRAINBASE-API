from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.exceptions import ProjectNotFoundError, TaskNotFoundError


async def task_not_found_exception_handler(
    _request: Request,
    exc: TaskNotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )

async def project_not_found_exception_handler(
    _request: Request,
    exc: ProjectNotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )