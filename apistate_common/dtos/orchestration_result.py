from typing import Generic, TypeVar, Optional
from ..enums.response_code import ResponseCode
from ..enums.response_status import ResponseStatus

T = TypeVar("T")

class OrchestrationResult(Generic[T]):
    def __init__(
        self,
        data: Optional[T],
        message: Optional[str],
        response_code: ResponseCode,
        response_status: ResponseStatus = ResponseStatus.UNKNOWN,
    ):
        """
        Represents the result of an operation, either successful or failed.

        :param data: The result data (if applicable).
        :param message: Error message (if applicable).
        :param response_code: Application-specific status code (ResponseCode).
        :param response_status: High-level success/failure response type (ResponseStatus).
        """
        self.data = data
        self.message = message
        self.response_code = response_code
        self.response_status = response_status

    @staticmethod
    def success(
        data: Optional[T],
        response_code: ResponseCode,
    ) -> "OrchestrationResult[T]":
        """Creates a successful response with optional data and an application-specific status code."""
        return OrchestrationResult(
            data=data,
            message=None,
            response_code=response_code,
            response_status=ResponseStatus.SUCCESS,
        )

    @staticmethod
    def failure(
        message: str,
        data: Optional[T],  # Allow optional data in failures
        response_code: ResponseCode,
    ) -> "OrchestrationResult[T]":
        """Creates a failure response with a message, an application-specific status code, and optional data."""
        return OrchestrationResult(
            message=message,
            response_code=response_code,
            response_status=ResponseStatus.FAILURE,
            data=data,  # Include data in failure case if needed
        )

    def __str__(self) -> str:
        return (
            f"OrchestrationResult(response_code={self.response_code}, "
            f"response_status={self.response_status}, message={self.message}, data={self.data})"
        )

    def is_success(self) -> bool:
        return self.response_status == ResponseStatus.SUCCESS

    def is_failure(self) -> bool:
        return self.response_status == ResponseStatus.FAILURE
