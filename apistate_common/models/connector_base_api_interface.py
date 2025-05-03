from abc import ABC, abstractmethod
from typing import List


class ConnectorBaseAPIInterface(ABC):
    def __init__(self):
        self.app = FastAPI()
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
                wrap_method(ConnectorBaseAPIInterface, self, method_name),
                methods=methods
            )

    # -------------------- Abstract Methods --------------------

    @abstractmethod
    async def health_check(self) -> dict:
        """Simple health check endpoint"""
        pass

    @abstractmethod
    async def check_credentials(self, credentials: dict) -> dict:
        """Validate API credentials"""
        pass

    @abstractmethod
    async def get_api_info(self, request: dict) -> list[dict]:
        """Retrieve information about a specific API"""
        pass

    @abstractmethod
    async def list_endpoints(self) -> list[dict]:
        """List available endpoints for the API"""
        pass