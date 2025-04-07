from pydantic import BaseModel
from typing import Optional, List

class OrganisationUnitBaseDto(BaseModel):
    """Base DTO for OrganisationUnit with common fields."""
    name: str

class OrganisationUnitCreateDto(OrganisationUnitBaseDto):
    """DTO for creating a new OrganisationUnit."""

class OrganisationUnitUpdateDto(BaseModel):
    """DTO for updating an existing OrganisationUnit."""
    name: Optional[str] = None

class OrganisationUnitResponseDto(OrganisationUnitBaseDto):
    """DTO for OrganisationUnit response."""
    id: str
    organisation: str

    class Config:
        from_attributes = True