from typing import Optional
from pydantic import BaseModel, Field
from .base import BaseDTO

class APIBaseDto(BaseDTO):
    """Base DTO for API data."""
    name: str = Field(..., description="API name")
    description: Optional[str] = Field(None, description="API description")
    version: str = Field(..., description="API version")
    project_id: str = Field(..., description="Project ID")
    connection_id: str = Field(..., description="Connection ID")
    connector_id: str = Field(..., description="Connector ID")
    url: Optional[str] = Field(None, description="API URL")

class APICreateDto(APIBaseDto):
    """DTO for creating a new API."""
    pass

class APIUpdateDto(BaseModel):
    """DTO for updating an existing API."""
    name: Optional[str] = Field(None, description="API name")
    description: Optional[str] = Field(None, description="API description")
    version: Optional[str] = Field(None, description="API version")
    # project_id: Optional[str] = Field(None, description="Project ID")
    # connection_id: Optional[str] = Field(None, description="Connection ID")
    # connector_id: Optional[str] = Field(None, description="Connector ID")
    status: Optional[str] = Field(None, description="API status")

class APIResponseDto(APIBaseDto):
    """DTO for API responses."""
    id: str = Field(..., description="API ID")
    organisation_id: str = Field(..., description="Organisation ID")
    status: str = Field(..., description="API status")