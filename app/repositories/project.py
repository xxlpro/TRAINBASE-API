from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, project_id: int) -> Project | None:
        stmt = select(Project).where(Project.id == project_id)
        return self.db.scalar(stmt)

    def get_list(self, *, offset: int = 0, limit: int = 100) -> list[Project]:
        stmt = select(Project).order_by(Project.id).offset(offset).limit(limit)

        return list(self.db.scalars(stmt).all())

    def create(self, payload: ProjectCreate) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
        )

        self.db.add(project)
        self.db.flush()

        return project

    def update(self, project: Project, payload: ProjectUpdate) -> Project:
        update_data = payload.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(project, field, value)

        self.db.flush()

        return project

    def delete(self, project: Project) -> None:
        self.db.delete(project)
        self.db.flush()

    def get_by_name(self, name: str) -> Project | None:
        stmt = select(Project).where(Project.name == name)
        return self.db.scalar(stmt)


    def get_by_name_except_id(self, name: str, project_id: int) -> Project | None:
        stmt = select(Project).where(
            Project.name == name,
            Project.id != project_id,
        )
        return self.db.scalar(stmt)
