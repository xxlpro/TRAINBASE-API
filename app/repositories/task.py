from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, task_id: int) -> Task | None:
        stmt = select(Task).where(Task.id == task_id)
        return self.db.scalar(stmt)

    def get_list(self, *, offset: int = 0, limit: int = 100) -> list[Task]:
        stmt = (
            select(Task)
            .order_by(Task.id)
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.scalars(stmt).all())

    def get_by_project_id(self, project_id: int) -> list[Task]:
        stmt = (
            select(Task)
            .where(Task.project_id == project_id)
            .order_by(Task.id)
        )
        return list(self.db.scalars(stmt).all())

    def create(self, payload: TaskCreate) -> Task:
        
        task = Task(
            title=payload.title,
            description=payload.description,
            project_id=payload.project_id,
        )

        self.db.add(task)
        self.db.flush()

        return task

    def update(self, task: Task, payload: TaskUpdate) -> Task:
        update_data = payload.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(task, field, value)

        self.db.flush()

        return task

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.flush()
