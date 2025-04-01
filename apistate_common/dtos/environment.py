from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EnvironmentBase(BaseModel):
    """Base DTO for Environment data."""
    name: str

class EnvironmentCreate(EnvironmentBase):
    """DTO for creating a new Environment."""
    pass

class EnvironmentUpdate(BaseModel):
    """DTO for updating an Environment."""
    name: Optional[str] = None

class EnvironmentResponse(EnvironmentBase):
    """DTO for Environment response data."""
    id: str
    organisation: str
    created_at: int
    updated_at: int
    created_by: str
    updated_by: Optional[str] = None

    class Config:
        from_attributes = True