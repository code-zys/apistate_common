from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    """DTO for login request data."""
    email: EmailStr
    password: str = Field(..., min_length=8)


class PasswordChangeRequest(BaseModel):
    """DTO for password change request data."""
    current_password: str = Field(..., min_length=8)
    new_password: str = Field(..., min_length=8)