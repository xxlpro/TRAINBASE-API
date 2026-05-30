from fastapi import APIRouter, Depends, Query, status

from app.api.dependencies import get_task_service
from app.schemas import TaskCreate, TaskRead, TaskUpdate
from app.services import TaskService
from app.api.responses import (
    PROJECT_NOT_FOUND_RESPONSE,
    TASK_NOT_FOUND_RESPONSE,
    TASK_OR_PROJECT_NOT_FOUND_RESPONSE,
)


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    responses=PROJECT_NOT_FOUND_RESPONSE,
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
    responses=TASK_NOT_FOUND_RESPONSE,
)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    return service.get_task(task_id)


@router.patch(
    "/{task_id}",
    response_model=TaskRead,
    responses=TASK_OR_PROJECT_NOT_FOUND_RESPONSE,
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
    responses=TASK_NOT_FOUND_RESPONSE,
)
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
) -> None:
    service.delete_task(task_id)