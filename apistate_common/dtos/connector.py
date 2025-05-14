from typing import List, Optional, Dict, Any, TypeVar, Generic
from pydantic import BaseModel
from datetime import datetime
from ..enums.connector_credentials_type import ConnectorCredentialsType

# Define a TypeVar for credentials
T = TypeVar('T')

# Input DTOs
class ConnectorCredentials(BaseModel, Generic[T]):
    """Generic credentials model for API connectors."""
    credentials: T 
    type: ConnectorCredentialsType

class ApiRequest(BaseModel, Generic[T]):
    """Generic request model for API operations."""
    credentials: T
    api_id: str
    version: str
    region: str

# Output DTOs
class HealthCheckResponse(BaseModel):
    """Health check response model."""
    status: str

class CredentialsCheckResponse(BaseModel):
    """Credentials validation response model."""
    status: str
    message: Optional[str] = None

class Version(BaseModel):
    """Version information model (replaces Stage for platform agnosticism)."""
    name: str
    version_id: Optional[str] = None  # Replaces deployment_id for more generic versioning
    description: Optional[str] = None
    last_updated_date: Optional[datetime] = None
    url: str
    metadata: Optional[Dict[str, Any]] = None  # Platform-specific additional information

class ApiInfo(BaseModel):
    """API information response model."""
    name: str
    id: str
    description: Optional[str] = None
    created_date: datetime
    version: Version
    metadata: Optional[Dict[str, Any]] = None  # Platform-specific additional information

class Endpoint(BaseModel):
    """API endpoint information model."""
    path: str
    method: str
    api_id: str
    resource_id: str
    query_params: Optional[dict] = None
    path_params: Optional[dict] = None
    body_type: Optional[dict] = None
    metadata: Optional[Dict[str, Any]] = None
    description: Optional[str] = None

class Version(BaseModel):
    """Environment information model."""
    name: str
    version_id: Optional[str] = None
    description: Optional[str] = None
    last_updated_date: Optional[datetime] = None
    url: str
    metadata: Optional[Dict[str, Any]] = None