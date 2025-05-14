from typing import List, Optional
from pydantic import BaseModel
from ..enums.request_body_check_operator import RequestBodyCheckOperator

class RequestBodyCheckDto(BaseModel):
    """DTO for request body check configuration"""
    path: str
    value: str
    operator: RequestBodyCheckOperator

class HealthCheckConfigCreateDto(BaseModel):
    """DTO for creating a health check configuration"""
    endpoint: Optional[str] = None
    cron: str
    status_code: int
    body_checks: List[RequestBodyCheckDto] = []
    api: str

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
    created_at: str
