from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import TaskService
from app.services.project import ProjectService


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)


def get_project_service(db: Session = Depends(get_db)) -> ProjectService:
    return ProjectService(db)
