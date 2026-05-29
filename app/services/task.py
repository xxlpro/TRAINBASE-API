from sqlalchemy.orm import Session

from app.core.exceptions import ProjectNotFoundError, TaskNotFoundError
from app.models.task import Task
from app.repositories.project import ProjectRepository
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = TaskRepository(db)
        self.project_repository = ProjectRepository(db)

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        return task

    def get_tasks(self, *, offset: int = 0, limit: int = 100) -> list[Task]:
        return self.repository.get_list(offset=offset, limit=limit)

    def create_task(self, payload: TaskCreate) -> Task:
        if payload.project_id is not None:
            project = self.project_repository.get_by_id(payload.project_id)
            if project is None:
                raise ProjectNotFoundError(payload.project_id)
        
        try:
            task = self.repository.create(payload)
            self.db.commit()
            self.db.refresh(task)
            return task
        except Exception:
            self.db.rollback()
            raise

    def update_task(self, task_id: int, payload: TaskUpdate) -> Task:
        task = self.repository.get_by_id(task_id)
        
        if task is None:
            raise TaskNotFoundError(task_id)

        if "project_id" in payload.model_fields_set:
            if payload.project_id is not None:
                project = self.project_repository.get_by_id(payload.project_id)
                if project is None:
                    raise ProjectNotFoundError(payload.project_id)

        try:
            updated_task = self.repository.update(task, payload)
            self.db.commit()
            self.db.refresh(updated_task)
            return updated_task
        except Exception:
            self.db.rollback()
            raise

    def delete_task(self, task_id: int) -> None:
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        try:
            self.repository.delete(task)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise