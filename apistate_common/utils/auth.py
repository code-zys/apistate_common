from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional, List
from pydantic import BaseModel

class TokenData(BaseModel):
    sub: str
    exp: Optional[int] = None
    organisation_id: Optional[str] = None
    member_type: Optional[str] = None
    user_id: Optional[str] = None

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

def validate_organization_access(token: str = Depends(oauth2_scheme), 
                              verify_token=None,
                              allowed_member_types: List[str] = None,
                              request = None):
    """
    Validate organization access and member type from JWT token
    
    Args:
        token: JWT token from request
        verify_token: Function to verify JWT token
        allowed_member_types: List of allowed member types. If empty, all types are allowed
        organisation_id: Organization ID to validate against token
        
    Returns:
        dict: Token payload if validation successful
        
    Raises:
        HTTPException: If token is invalid or access is denied
    """
    if not verify_token:
        raise ValueError("verify_token function must be provided")
        
    try:
        payload = verify_token(token)
        
        # Extract and validate organization ID from path parameters
        if not request or not hasattr(request, "path_params") or "organisation_id" not in request.path_params:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Organization ID is required in path parameters",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        organisation_id = request.path_params["organisation_id"]
        token_org_id = payload.get("organisation_id")
        if not token_org_id or token_org_id != organisation_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied for this organization",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Validate member type if specified and not empty
        if allowed_member_types and len(allowed_member_types) > 0:
            member_type = payload.get("member_type")
            if not member_type or member_type not in allowed_member_types:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="User type not authorized for this operation",
                    headers={"WWW-Authenticate": "Bearer"},
                )
                
        return payload
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )