from typing import Optional
from pydantic import BaseModel, Field
from .base import BaseDTO

class OrganisationDTO(BaseDTO):
    """DTO for Organisation data."""
    name: str = Field(..., description="Organisation name")
    code: str = Field(..., description="Organisation unique code")
    domain: str = Field(..., description="Organisation domain")

class OrganisationCreateDTO(BaseDTO):
    """DTO for Organisation creation."""
    name: str = Field(..., description="Organisation name")
    code: str = Field(..., description="Organisation unique code")
    domain: str = Field(..., description="Organisation domain")