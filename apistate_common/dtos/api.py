from typing import Optional
from pydantic import BaseModel, Field
from .base import BaseDTO

class APIBaseDto(BaseModel):
    """Base DTO for API with common fields."""
    name: str = Field(..., description="API name")
    version: str = Field(..., description="API version")
    project: str = Field(..., description="Project ID")

class APICreateDto(APIBaseDto):
    """DTO for creating a new API."""
    pass

class APIUpdateDto(BaseModel):
    """DTO for updating an existing API."""
    name: Optional[str] = Field(None, description="API name")
    version: Optional[str] = Field(None, description="API version")
    project: Optional[str] = Field(None, description="Project ID")

class APIResponseDto(APIBaseDto, BaseDTO):
    """DTO for API responses."""
    pass