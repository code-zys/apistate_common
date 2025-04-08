from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from .base import BaseDTO
from ..enums.user_type import UserType
class UserDTO(BaseDTO):
    """DTO for User data."""
    email: EmailStr = Field(..., description="User email")
    first_name: Optional[str] = Field(None, description="User first name")
    last_name: Optional[str] = Field(None, description="User last name")
    is_active: bool = Field(True, description="User active status")
    type: UserType = Field(..., description="User type")

class UserCreateDto(BaseModel):
    """DTO for creating a new user."""
    email: EmailStr
    password: str
    first_name: str = Field(..., description="User first name")
    last_name: str = Field(..., description="User last name")
    is_active: bool = Field(..., description="User  is active or not")
    change_password_on_first_connection: bool = Field(..., description="change_password_on_first_connection")
    type: UserType = Field(..., description="User type")

class UserUpdateDto(BaseModel):
    """DTO for updating a user."""
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    change_password_on_first_connection: Optional[bool] = None
    hashed_password: Optional[str] = None
    type: Optional[UserType] = None

class UserResponseDto(BaseModel):
    """DTO for user response."""
    id: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[UserType] = None
    is_active: bool
    created_at: str
    updated_at: str
