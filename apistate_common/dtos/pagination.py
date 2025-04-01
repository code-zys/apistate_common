from typing import Optional, List, Dict, Any
from pydantic import BaseModel

class PaginatedResponse(BaseModel):
    """Standard paginated response format."""
    items: List[Any]
    total: int
    page: int
    size: int

class ErrorResponse(BaseModel):
    """Standard error response format."""
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None