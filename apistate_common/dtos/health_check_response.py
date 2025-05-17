from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime
from apistate_common.enums.api_status import APIStatus

class HealthCheckResponseDto(BaseModel):
    timestamp: datetime
    req_status: int
    request: Dict[str, Any]
    response: Dict[str, Any]
    api_status: APIStatus
    api: str
    config: str
    request_duration: int