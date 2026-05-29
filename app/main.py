from fastapi import FastAPI

from app.api.exception_handlers import app_error_handler
from app.api.routers.health import router as health_router
from app.api.routers.projects import router as projects_router
from app.api.routers.tasks import router as tasks_router
from app.core.config import get_settings
from app.core.exceptions import AppError


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.add_exception_handler(
    AppError,
    app_error_handler,
)

app.include_router(health_router)
app.include_router(tasks_router)
app.include_router(projects_router)