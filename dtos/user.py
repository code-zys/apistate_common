from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from .base import BaseDTO

class UserDTO(BaseDTO):
    """DTO for User data."""
    email: EmailStr = Field(..., description="User email")
    first_name: Optional[str] = Field(None, description="User first name")
    last_name: Optional[str] = Field(None, description="User last name")
    is_active: bool = Field(True, description="User active status")
    is_superuser: bool = Field(False, description="Superuser status")