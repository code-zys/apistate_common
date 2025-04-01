from typing import Generic, TypeVar, Optional, Union

from .enum_response import EnumStatusResponse, EnumStatusCode
from .exception import GenericException

T = TypeVar('T')


class OrchestrationResult(Generic[T]):
    def __init__(self, data: Union[T, str], statusCode: EnumStatusCode, code: Optional[EnumStatusResponse] = None):
        self.code = code
        self.statusCode = statusCode
        if isinstance(data, str):
            self.message = data
            self.data = None
        else:
            self.data = data
            self.message = None
    @staticmethod
    def Success(statusCode: EnumStatusCode, val: Union[T, str] = True, code: EnumStatusResponse = EnumStatusResponse.SUCCESS) -> 'OrchestrationResult[T]':
        return OrchestrationResult(val, statusCode, code)
    @staticmethod
    def GenericError(exception: GenericException) -> 'OrchestrationResult[T]':
        return OrchestrationResult.Failure(exception.message, exception.statusCode)
    def Failure(message: str, statusCode: EnumStatusCode, code: EnumStatusResponse = EnumStatusResponse.FAILURE) -> 'OrchestrationResult[T]':
        return OrchestrationResult(message, statusCode, code)
    def __str__(self) -> str:
        return f"OrchestrationResult (code: {self.code}, statusCode: {self.statusCode}, message: {self.message}, data: {self.data})"
    def is_success(self) -> bool:
        return self.code == EnumStatusResponse.SUCCESS
    def is_failure(self) -> bool:
        return self.code == EnumStatusResponse.FAILURE