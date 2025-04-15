from typing import List, Optional, Union
from fastapi import HTTPException, status
from jose import JWTError, jwt
from ..dtos.permission import OrganisationPermissionDTO, OrganisationalUnitPermissionDTO
from datetime import datetime
class BaseTokenValidator:
    def __init__(self, secret_key: str):
        if not secret_key:
            raise ValueError("secret_key must be provided")
        self.secret_key = secret_key
    
    @staticmethod
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
        

    async def validate_token(self, token: str, request, required_abilities: Optional[List[Union[OrganisationPermissionDTO, OrganisationalUnitPermissionDTO]]] = None, id_param: str = None):
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Token header is required",
                headers={"WWW-Authenticate": "Bearer"},
            )

        try:
            payload = verify_token(token, self.secret_key)
            self._validate_id_in_path(request, id_param)
            self._validate_access(payload, request.path_params[id_param], id_param)
            
            if required_abilities:
                self._validate_abilities(payload, required_abilities)
                
            return payload
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    def _validate_id_in_path(self, request, id_param: str):
        if not request or not hasattr(request, "path_params") or id_param not in request.path_params:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"ID parameter {id_param} is required in path parameters",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    def _validate_access(self, payload: dict, path_id: str, id_field: str):
        token_id = payload.get(id_field)
        if not token_id or token_id != path_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied for this resource",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    def _validate_abilities(self, payload: dict, required_abilities: List[Union[OrganisationPermissionDTO, OrganisationalUnitPermissionDTO]]):
        abilities_field = "organisation_abilities" if isinstance(required_abilities[0], OrganisationPermissionDTO) else "organisational_unit_abilities"
        user_abilities = payload.get(abilities_field, [])
        
        for required_permission in required_abilities:
            permission_found = False
            for user_ability in user_abilities:
                if self._check_permission(user_ability, required_permission):
                    permission_found = True
                    break
                    
            if not permission_found:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Missing required permission for resource type: {required_permission.resource_type.value}",
                    headers={"WWW-Authenticate": "Bearer"},
                )
    
    def _check_permission(self, user_ability: dict, required_permission) -> bool:
        if (user_ability.get("actions", []) == ["ALL"] and 
            (user_ability.get("resource_type") == "ALL" or 
             user_ability.get("resource_type") == required_permission.resource_type.value)):
            return True
            
        return (user_ability.get("resource_type") == required_permission.resource_type.value and
                all(action.value in user_ability.get("actions", []) 
                    for action in required_permission.actions))