from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.schemas.error import ErrorResponse, ErrorDetail

__all__ = (
    "TaskCreate",
    "TaskRead",
    "TaskUpdate",
    "ProjectUpdate",
    "ProjectRead",
    "ProjectCreate",
    "ErrorDetail",
    "ErrorResponse",
)
