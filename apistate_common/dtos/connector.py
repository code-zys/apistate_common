from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime

# Input DTOs
class ConnectorCredentials(BaseModel):
    """Generic credentials model for API connectors."""
    credentials: Dict[str, Any]  # Flexible credentials structure for different platforms

class ApiRequest(BaseModel):
    """Generic request model for API operations."""
    credentials: Dict[str, Any]  # Flexible credentials structure
    api_id: str

# Output DTOs
class HealthCheckResponse(BaseModel):
    """Health check response model."""
    status: str

class CredentialsCheckResponse(BaseModel):
    """Credentials validation response model."""
    status: str
    message: Optional[str] = None

class Environment(BaseModel):
    """Environment information model (replaces Stage for platform agnosticism)."""
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
    environments: List[Environment]  # Replaces stages with more generic environments
    metadata: Optional[Dict[str, Any]] = None  # Platform-specific additional information

class Endpoint(BaseModel):
    """API endpoint information model."""
    path: str
    method: str
    api_id: str
    resource_id: str
    metadata: Optional[Dict[str, Any]] = None  # Platform-specific additional information