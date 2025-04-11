from pydantic import BaseModel
from typing import Optional

class UserTokenDto(BaseModel):
    """Data transfer object for user token data"""
    sub: str
    user_id: str
    email: str
    type: str
    token_type: Optional[str] = None