from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict

class ProjectCreate(BaseModel):
    """DTO for creating a new project."""
    name: str
    description: str | None = None
    environment: str | None = None
    config_file: str | None = None  # API configuration JSON
    organisational_unit: str | None = None

class ProjectUpdate(BaseModel):
    """DTO for updating an existing project."""
    name: str | None = None
    description: str | None = None
    environment: str | None = None
    config_file: str | None = None  # API configuration JSON

class ProjectResponse(BaseModel):
    """DTO for project response."""
    id: str
    name: str
    description: str | None = None
    organisation: str
    environment: str | None = None
    config_file: Dict | None = None  # API configuration as dictionary
    organisational_unit: str | None = None
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str | None = None

    class Config:
        from_attributes = True