from pydantic import BaseModel
from typing import Dict, Any
from apistate_common.enums.api_status import APIStatus

class HealthCheckResponseDto(BaseModel):
    timestamp: int
    status_code: int
    api_status: APIStatus
    request: Dict[str, Any]
    response: Dict[str, Any]
    config_id: str