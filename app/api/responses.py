from fastapi import status

from app.schemas import ErrorResponse


TASK_NOT_FOUND_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Task not found",
        "content": {
            "application/json": {
                "example": {
                    "error": {
                        "code": "task_not_found",
                        "message": "Task with id=999 was not found",
                    }
                }
            }
        },
    }
}


PROJECT_NOT_FOUND_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Project not found",
        "content": {
            "application/json": {
                "example": {
                    "error": {
                        "code": "project_not_found",
                        "message": "Project with id=999 was not found",
                    }
                }
            }
        },
    }
}


TASK_OR_PROJECT_NOT_FOUND_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorResponse,
        "description": "Task or project not found",
        "content": {
            "application/json": {
                "examples": {
                    "task_not_found": {
                        "summary": "Task not found",
                        "value": {
                            "error": {
                                "code": "task_not_found",
                                "message": "Task with id=999 was not found",
                            }
                        },
                    },
                    "project_not_found": {
                        "summary": "Project not found",
                        "value": {
                            "error": {
                                "code": "project_not_found",
                                "message": "Project with id=999 was not found",
                            }
                        },
                    },
                }
            }
        },
    }
}