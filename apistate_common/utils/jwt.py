from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from pydantic import BaseModel

class TokenData(BaseModel):
    sub: str
    exp: Optional[int] = None

class JWTHandler:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """
        Create a JWT token
        
        Args:
            data: Data to encode in token
            expires_delta: Optional expiration time
            
        Returns:
            JWT token as string
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> dict:
        """
        Verify and decode a JWT token
        
        Args:
            token: JWT token to verify
            
        Returns:
            Decoded token data
            
        Raises:
            JWTError: If token is invalid
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            if payload.get("sub") is None:
                raise JWTError("Token missing subject claim")
            token_data = TokenData(**payload)
            return payload
        except JWTError as e:
            raise JWTError(f"Could not validate credentials: {str(e)}")