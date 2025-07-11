from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict
from fastapi import Form, File, UploadFile

class ProjectCreate(BaseModel):
    """DTO for creating a new project."""
    name: str
    description: str | None = None
    environment: str | None = None
    config_file: UploadFile  # API configuration JSON
    organisational_unit: str | None = None

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        description: Optional[str] = Form(None),
        config_file: UploadFile = File(...),
        environment= Form(...),
        organisational_unit: Optional[str] = Form(None)
    ):
        return cls(name=name, description=description, config_file=config_file, environment=environment, organisational_unit=organisational_unit)

class ProjectUpdate(BaseModel):
    """DTO for updating an existing project."""
    name: str | None = None
    description: str | None = None
    environment: str | None = None
    config_file: UploadFile  # API configuration JSON

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