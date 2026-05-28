from sqlalchemy.orm import Session

from app.core.exceptions import TaskNotFoundError
from app.models.task import Task
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = TaskRepository(db)

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        return task

    def get_tasks(self, *, offset: int = 0, limit: int = 100) -> list[Task]:
        return self.repository.get_list(offset=offset, limit=limit)

    def create_task(self, payload: TaskCreate) -> Task:
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