from pydantic import BaseModel
from typing import Optional, List

class OrganisationalUnitBaseDto(BaseModel):
    """Base DTO for OrganisationUnit with common fields."""
    name: str
    description: Optional[str] = None

class OrganisationalUnitCreateDto(OrganisationalUnitBaseDto):
    """DTO for creating a new OrganisationUnit."""

class OrganisationalUnitUpdateDto(BaseModel):
    """DTO for updating an existing OrganisationUnit."""
    name: Optional[str] = None
    description: Optional[str] = None

class OrganisationalUnitResponseDto(OrganisationalUnitBaseDto):
    """DTO for OrganisationUnit response."""
    id: str
    organisation: str

    class Config:
        from_attributes = True