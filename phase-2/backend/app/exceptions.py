from typing import Optional, Dict, Any
from fastapi import HTTPException, status
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Standardized error response format."""
    error: Dict[str, Any]


class TodoException(HTTPException):
    """Base exception class for todo application with standardized error format."""

    def __init__(
        self,
        status_code: int,
        message: str,
        code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ):
        error_data = {
            "message": message,
            "code": code or f"ERR_{status_code}",
        }
        if details:
            error_data["details"] = details

        response = ErrorResponse(error=error_data)

        super().__init__(
            status_code=status_code,
            detail=response.model_dump(),
        )


class UnauthorizedException(TodoException):
    """Exception for unauthorized access (401)."""

    def __init__(self, message: str = "Unauthorized", details: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message=message,
            code="UNAUTHORIZED",
            details=details
        )


class ForbiddenException(TodoException):
    """Exception for forbidden access (403)."""

    def __init__(self, message: str = "Forbidden", details: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            message=message,
            code="FORBIDDEN",
            details=details
        )


class NotFoundException(TodoException):
    """Exception for resource not found (404)."""

    def __init__(self, message: str = "Not Found", details: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message=message,
            code="NOT_FOUND",
            details=details
        )


class ValidationException(TodoException):
    """Exception for validation errors (422)."""

    def __init__(self, message: str = "Validation Error", details: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=message,
            code="VALIDATION_ERROR",
            details=details
        )


class BadRequestException(TodoException):
    """Exception for bad requests (400)."""

    def __init__(self, message: str = "Bad Request", details: Optional[Dict[str, Any]] = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=message,
            code="BAD_REQUEST",
            details=details
        )