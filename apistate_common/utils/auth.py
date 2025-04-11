from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional, List
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime
from apistate_common.dtos.token import UserTokenDto

class TokenData(BaseModel):
    sub: str
    exp: Optional[int] = None
    organisation_id: Optional[str] = None
    member_type: Optional[str] = None
    user_id: Optional[str] = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str, secret_key: str, algorithm: str = "HS256") -> dict:
    """
    Verify and decode JWT token
    
    Args:
        token: JWT token to verify
        secret_key: Secret key used to sign the token
        algorithm: Algorithm used to sign the token (default: HS256)
        
    Returns:
        dict: Decoded token payload
        
    Raises:
        HTTPException: If token is invalid or expired
    """
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        
        # Verify required claims
        if "sub" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token claims",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        # Verify expiration
        exp = payload.get("exp")
        if exp and datetime.fromtimestamp(exp) < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        return payload
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},)
        
def get_current_user(secret_key: str = None):
    """
    Factory function that returns a function to get current user from JWT token
    
    Args:
        secret_key: Secret key used to sign the token
        
    Returns:
        function: A function that takes a token and returns UserTokenDto
        
    Raises:
        ValueError: If secret_key is not provided
    """
    if not secret_key:
        raise ValueError("secret_key must be provided")
        
    def get_user(token: str = Depends(oauth2_scheme)) -> UserTokenDto:
        """
        Get current user from JWT token
        
        Args:
            token: JWT token from request
            
        Returns:
            UserTokenDto: User token data transfer object
            
        Raises:
            HTTPException: If token is invalid
        """
        payload = verify_token(token, secret_key)
        return UserTokenDto(
            sub=payload["sub"],
            user_id=payload["user_id"],
            email=payload["sub"],
            type=payload["type"]
        )
    return get_user

def validate_organization_access(token: str = Depends(oauth2_scheme), 
                              secret_key: str = None,
                              allowed_member_types: List[str] = None,
                              request = None,
                              org_id_param: str = "organisation_id"):
    """
    Validate organization access and member type from JWT token
    
    Args:
        token: JWT token from request
        secret_key: Secret key used to sign the token
        allowed_member_types: List of allowed member types. If empty, all types are allowed
        request: FastAPI request object containing path parameters
        org_id_param: Name of the path parameter containing organization ID (default: 'organisation_id')
        
    Returns:
        dict: Token payload if validation successful
        
    Raises:
        HTTPException: If token is invalid or access is denied
    """
    if not secret_key:
        raise ValueError("secret_key must be provided")
        
    try:
        payload = verify_token(token, secret_key)
        
        # Extract and validate organization ID from path parameters
        if not request or not hasattr(request, "path_params") or org_id_param not in request.path_params:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Organization ID is required in path parameters",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        organisation_id = request.path_params[org_id_param]
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