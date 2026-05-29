class AppError(Exception):
    """Base application exception."""


class TaskNotFoundError(AppError):
    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task with id={task_id} was not found")


class ProjectNotFoundError(AppError):
    def __init__(self, project_id: int) -> None:
        self.project_id = project_id
        super().__init__(f"Project with id={project_id} was not found")