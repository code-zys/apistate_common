from typing import Optional
from pydantic import BaseModel, Field

class BaseDTO(BaseModel):
    """Base DTO class with common fields."""
    id: Optional[str] = Field(None, description="Document ID")
    created_at: Optional[int] = Field(None, description="Creation timestamp")
    updated_at: Optional[int] = Field(None, description="Last update timestamp")
    created_by: Optional[str] = Field(None, description="Creator user ID")
    updated_by: Optional[str] = Field(None, description="Last updater user ID")