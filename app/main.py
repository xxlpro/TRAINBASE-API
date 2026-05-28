from fastapi import FastAPI

from app.api.exception_handlers import task_not_found_exception_handler
from app.api.routers.health import router as health_router
from app.api.routers.tasks import router as tasks_router
from app.core.config import get_settings
from app.core.exceptions import TaskNotFoundError


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.add_exception_handler(
    TaskNotFoundError,
    task_not_found_exception_handler,
)

app.include_router(health_router)
app.include_router(tasks_router)