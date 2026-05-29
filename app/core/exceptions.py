class AppError(Exception):
    status_code: int = 500
    code: str = "app_error"
    message: str = "Application error"

    def __init__(self, message: str | None = None) -> None:
        if message is not None:
            self.message = message

        super().__init__(self.message)


class TaskNotFoundError(AppError):
    status_code = 404
    code = "task_not_found"

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id
        super().__init__(f"Task with id={task_id} was not found")


class ProjectNotFoundError(AppError):
    status_code = 404
    code = "project_not_found"

    def __init__(self, project_id: int) -> None:
        self.project_id = project_id
        super().__init__(f"Project with id={project_id} was not found")