from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from pydantic import BaseModel

class TokenData(BaseModel):
    sub: str
    exp: Optional[int] = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), verify_token=None, get_user_by_email=None):
    """
    Get current user from JWT token
    
    Args:
        token: JWT token from request
        verify_token: Function to verify JWT token
        get_user_by_email: Function to get user by email
        
    Returns:
        User object if token is valid
        
    Raises:
        HTTPException: If token is invalid or user not found
    """
    if not verify_token or not get_user_by_email:
        raise ValueError("verify_token and get_user_by_email functions must be provided")
        
    payload = verify_token(token)
    user = get_user_by_email(payload["sub"])
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def get_current_active_user(current_user, is_active_field: str = "is_active"):
    """
    Check if current user is active
    
    Args:
        current_user: User object to check
        is_active_field: Name of the field that indicates if user is active
        
    Returns:
        User object if active
        
    Raises:
        HTTPException: If user is inactive
    """
    if not getattr(current_user, is_active_field, True):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user