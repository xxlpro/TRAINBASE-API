from sqlalchemy.orm import Session

from app.core.exceptions import ProjectNotFoundError
from app.models.project import Project
from app.models.task import Task
from app.repositories.project import ProjectRepository
from app.repositories.task import TaskRepository
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = ProjectRepository(db)
        self.task_repository = TaskRepository(db)

    def get_project(self, project_id: int) -> Project:
        project = self.repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        return project
    
    def get_projects(self, offset: int, limit: int) -> list[Project]:
        return self.repository.get_list(offset=offset, limit=limit)
    
    def get_project_tasks(self, project_id: int) -> list[Task]:
        project = self.repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)
        
        return self.task_repository.get_by_project_id(project_id)

    def create_project(self, payload: ProjectCreate) -> Project:
        try:
            project = self.repository.create(payload)
            self.db.commit()
            self.db.refresh(project)
            return project
        except Exception:
            self.db.rollback()
            raise

    def update_project(self, project_id: int, payload: ProjectUpdate) -> Project:
        project = self.repository.get_by_id(project_id)

        if project is None: 
            raise ProjectNotFoundError(project_id)
        
        try:
            updated_project = self.repository.update(project, payload)
            self.db.commit()
            self.db.refresh(updated_project)
            return updated_project
        except Exception:
            self.db.rollback()
            raise

    def delete_project(self, project_id: int) -> None:
        project = self.repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)
        
        try:
            self.repository.delete(project)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    
