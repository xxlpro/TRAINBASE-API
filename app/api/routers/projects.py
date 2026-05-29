from fastapi import APIRouter, Query, Depends, status


from app.api.dependencies import get_project_service
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.schemas.task import TaskRead
from app.services.project import ProjectService


router = APIRouter(prefix="/projects", tags=["Project"])


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
    "/{project_id}",
    response_model=ProjectRead,
)
def get_project(
    project_id: int,
    service: ProjectService = Depends(get_project_service),
):
    return service.get_project(project_id)


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


@router.get(
        "/{project_id}/tasks",
        response_model=list[TaskRead],
)
def get_project_tasks(
    project_id: int,
    service: ProjectService = Depends(get_project_service),
):
    return service.get_project_tasks(project_id)


@router.patch(
    "/{project_id}",
    response_model=ProjectRead,
)
def update_project(
    project_id: int,
    payload: ProjectUpdate,
    service: ProjectService = Depends(get_project_service),
):
    return service.update_project(project_id, payload)


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project(
    project_id: int,
    service: ProjectService = Depends(get_project_service)
):
    service.delete_project(project_id)