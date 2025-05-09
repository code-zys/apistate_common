from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from fastapi import FastAPI
from ..dtos.connector import (
    HealthCheckResponse,
    ConnectorCredentials,
    ApiRequest,
    CredentialsCheckResponse,
    ApiInfo,
    Endpoint
)
from ..utils.connector_api_type_checker import ConnectorAPITypeChecker
from ..dtos.orchestration_result import OrchestrationResult

CredentialsType = TypeVar('CredentialsType')

class ConnectorBaseAPIInterface(ABC, Generic[CredentialsType]):
    def __init__(self, app: FastAPI = None):
        """Initialize the connector with an optional FastAPI instance.
        
        Args:
            app: FastAPI instance to register routes on. If None, creates a new instance.
        """
        self.app = app if app is not None else FastAPI()
        self._register_routes()

    def _register_routes(self):
        routes = [
            ("/health", "health_check", ["GET"]),
            ("/credentials/check", "check_credentials", ["POST"]),
            ("/info", "get_api_info", ["POST"]),
            ("/endpoints", "list_endpoints", ["GET"]),
        ]

        for path, method_name, methods in routes:
            self.app.add_api_route(
                path,
                ConnectorAPITypeChecker.wrap_method(ConnectorBaseAPIInterface, self, method_name),
                methods=methods
            )

    # -------------------- Abstract Methods --------------------

    @abstractmethod
    async def health_check(self) -> OrchestrationResult[HealthCheckResponse]:
        """Simple health check endpoint"""
        pass

    @abstractmethod
    async def check_credentials(self, credentials: ConnectorCredentials[CredentialsType]) -> CredentialsCheckResponse:
        """Validate API credentials"""
        pass

    @abstractmethod
    async def get_api_info(self, request: ApiRequest[CredentialsType]) -> ApiInfo:
        """Retrieve information about a specific API"""
        pass

    @abstractmethod
    async def list_endpoints(self, request: ApiRequest[CredentialsType]) -> List[Endpoint]:
        """List available endpoints for the API"""
        pass

    def get_app(self) -> FastAPI:
        """Get the FastAPI application instance"""
        return self.app