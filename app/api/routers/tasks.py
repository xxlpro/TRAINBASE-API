from fastapi import APIRouter, Depends, Query, status

from app.api.dependencies import get_task_service
from app.schemas import TaskCreate, TaskRead, TaskUpdate
from app.services import TaskService


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    payload: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    return service.create_task(payload)


@router.get(
    "",
    response_model=list[TaskRead],
)
def get_tasks(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    service: TaskService = Depends(get_task_service),
):
    return service.get_tasks(offset=offset, limit=limit)


@router.get(
    "/{task_id}",
    response_model=TaskRead,
)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    return service.get_task(task_id)


@router.patch(
    "/{task_id}",
    response_model=TaskRead,
)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    return service.update_task(task_id, payload)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
) -> None:
    service.delete_task(task_id)