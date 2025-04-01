from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    """DTO for creating a new project."""
    name: str
    description: str | None = None

class ProjectUpdate(BaseModel):
    """DTO for updating an existing project."""
    name: str | None = None
    description: str | None = None

class ProjectResponse(BaseModel):
    """DTO for project response."""
    id: str
    name: str
    description: str | None = None
    organisation: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str | None = None

    class Config:
        from_attributes = True