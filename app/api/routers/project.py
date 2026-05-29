from fastapi import APIRouter, Query, Depends, status


from app.api.dependencies import get_project_service
from app.schemas.project import ProjectCreate, ProjectRead
from app.services.project import ProjectService


router = APIRouter(prefix="/project", tags=["Project"])


@router.post(
        "",
        response_model=ProjectRead,
        status_code=status.HTTP_201_CREATED,
)
def create_project(
    payload: ProjectCreate,
    service: ProjectService = Depends(get_project_service)
):
    return service.create_project(payload)


@router.get(
"",
response_model=list[ProjectRead],
)
def get_projects(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    service: ProjectService = Depends(get_project_service),
):
    return service.get_projects(offset=offset, limit=limit)