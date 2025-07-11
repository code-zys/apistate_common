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
    endpoint: str
    cron: str
    api: str
    path_params_data: Optional[dict] = {}
    query_params_data: Optional[dict] = {}

class HealthCheckConfigUpdateDto(BaseModel):
    """DTO for updating a health check configuration"""
    endpoint_id: Optional[str] = None
    cron: Optional[str] = None
    status_code: Optional[int] = None
    body_checks: Optional[List[RequestBodyCheckDto]] = None
    path_params_data: Optional[dict] = None
    query_params_data: Optional[dict] = None

class HealthCheckConfigResponseDto(BaseModel):
    """DTO for health check configuration response"""
    id: str
    endpoint_id: Optional[str]
    cron: str
    api_id: str    
    created_at: Optional[int] = None
    path_params_data: dict = {}
    query_params_data: dict = {}
