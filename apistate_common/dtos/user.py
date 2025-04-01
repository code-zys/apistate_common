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


class UserCreateDto(BaseModel):
    """DTO for creating a new user."""
    email: EmailStr
    password: str

class UserUpdateDto(BaseModel):
    """DTO for updating a user."""
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

class UserResponseDto(BaseModel):
    """DTO for user response."""
    id: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: bool
    is_superuser: bool
    created_at: str
    updated_at: str
