from sqlalchemy.orm import Session

from app.models.project import Project
from app.repositories.project import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectRead


class ProjectService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = ProjectRepository(db)

    def get_projects(self, offset: int, limit: int) -> list[Project]:
        return self.repository.get_list(offset=offset, limit=limit)

    def create_project(self, payload: ProjectCreate) -> Project:
        try:
            project = self.repository.create(payload)
            self.db.commit()
            self.db.refresh(project)
            return project
        except Exception:
            self.db.rollback()
            raise

    
