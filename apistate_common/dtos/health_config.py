from typing import List, Optional
from pydantic import BaseModel

class RequestBodyCheckDto(BaseModel):
    """DTO for request body check configuration."""
    path: str
    expected_value: str

class HealthCheckConfigResponseDto(BaseModel):
    """DTO for health check configuration response."""
    id: str
    endpoint_id: Optional[str]
    cron: str
    status_code: int
    body_checks: List[RequestBodyCheckDto]
    api_id: str