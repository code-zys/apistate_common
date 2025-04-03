from pydantic import BaseModel, Field
from typing import Optional
from ..enums.member_type import MemberType

class MemberCreateDto(BaseModel):
    """DTO for creating a new member."""
    user_id: str
    organization_id: str
    member_type: MemberType

class MemberUpdateDto(BaseModel):
    """DTO for updating a member."""
    member_type: Optional[str] = None

class UserInfo(BaseModel):
    """Nested DTO for user information."""
    id: str
    email: str
    first_name: str
    last_name: str

class OrganizationInfo(BaseModel):
    """Nested DTO for organization information."""
    id: str
    name: str
    code: str
    domain: str

class MemberResponseDto(BaseModel):
    """DTO for member response."""
    id: str
    member_type: str
    created_at: str
    updated_at: str
    user: UserInfo
    organization: OrganizationInfo
    
    class Config:
        from_attributes = True