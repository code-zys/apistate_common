from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from typing import Optional, List
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime
from apistate_common.dtos.token import UserTokenDto
from apistate_common.enums.user_type import UserType
from apistate_common.dtos.permission import OrganisationPermissionDTO, OrganisationalUnitPermissionDTO
from .token_validator import BaseTokenValidator

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
        

def get_current_user(secret_key: str, allowed_types: List[UserType] = None):
    """
    Factory function that returns a function to get current user from JWT token
    
    Args:
        secret_key: Secret key used to sign the token
        allowed_types: List of allowed user types. If empty or None, all types are allowed
        
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
            HTTPException: If token is invalid or user type not authorized
        """
        payload = verify_token(token, secret_key)
        user_type = payload.get("type")
        
        # Validate user type if allowed_types is specified and not empty
        if allowed_types and len(allowed_types) > 0:
            if not user_type or user_type not in [t.value for t in allowed_types]:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="User type not authorized for this operation",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        
        return UserTokenDto(
            sub=payload["sub"],
            user_id=payload["user_id"],
            email=payload["sub"],
            type=user_type
        )
    return get_user


def validate_organisation_token(secret_key: str, required_abilities: List[OrganisationPermissionDTO] = None):
    validator = BaseTokenValidator(secret_key)
    
    async def validate(organisation_token: str = Header(None, alias="OrganisationToken"), request = None):
        return await validator.validate_token(
            token=organisation_token,
            request=request,
            required_abilities=required_abilities,
            id_param="organisation_id"
        )
    return validate

def validate_organisational_unit_token(secret_key: str, required_abilities: List[OrganisationalUnitPermissionDTO] = None):
    validator = BaseTokenValidator(secret_key)
    
    async def validate(organisational_unit_token: str = Header(None, alias="OrganisationalUnitToken"), request = None):
        return await validator.validate_token(
            token=organisational_unit_token,
            request=request,
            required_abilities=required_abilities,
            id_param="organisational_unit_id"
        )
    return validate

