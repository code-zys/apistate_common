from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import List, TypeVar, Generic, Dict
from fastapi import FastAPI
from ..dtos.connector import (
    HealthCheckResponse,
    ConnectorCredentials,
    CredentialsCheckResponse,
)
from ..utils.connector_api_type_checker import ConnectorAPITypeChecker
from ..dtos.orchestration_result import OrchestrationResult

CredentialsType = TypeVar('CredentialsType')

class SwaggerConnector(BaseModel):
    url: str 
    bucket: str
    object_key: str

class SwaggerConnectorBaseAPIInterface(ABC, Generic[CredentialsType]):
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
            ("/get-swagger", "get_swagger_file", ["POST"]),
        ]

        for path, method_name, methods in routes:
            self.app.add_api_route(
                path,
                ConnectorAPITypeChecker.wrap_method(SwaggerConnectorBaseAPIInterface, self, method_name),
                methods=methods
            )

    # -------------------- Abstract Methods --------------------

    @abstractmethod
    async def health_check(self) -> HealthCheckResponse:
        """Simple health check endpoint"""
        pass

    @abstractmethod
    async def check_credentials(self, credentials: ConnectorCredentials[CredentialsType]) -> CredentialsCheckResponse:
        """Validate API credentials"""
        pass

    @abstractmethod
    async def get_swagger_file(self, connection_id: str, data: SwaggerConnector) -> Dict:
        """Retrieve Swagger file """
        pass

    def get_app(self) -> FastAPI:
        """Get the FastAPI application instance"""
        return self.app