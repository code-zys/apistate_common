from typing import List, Optional
from pydantic import BaseModel

class RequestBodyCheckDto(BaseModel):
    """DTO for request body check configuration"""
    path: str
    expected_value: str

class HealthCheckConfigCreateDto(BaseModel):
    """DTO for creating a health check configuration"""
    endpoint_id: Optional[str] = None
    cron: str
    status_code: int
    body_checks: List[RequestBodyCheckDto] = []
    api_id: str

class HealthCheckConfigUpdateDto(BaseModel):
    """DTO for updating a health check configuration"""
    endpoint_id: Optional[str] = None
    cron: Optional[str] = None
    status_code: Optional[int] = None
    body_checks: Optional[List[RequestBodyCheckDto]] = None

class HealthCheckConfigResponseDto(BaseModel):
    """DTO for health check configuration response"""
    id: str
    endpoint_id: Optional[str]
    cron: str
    status_code: int
    body_checks: List[RequestBodyCheckDto]
    api_id: str