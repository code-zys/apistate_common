from typing import Optional
from pydantic import BaseModel
from ..enums.endpoint_method_type import EndpointMethodType

class EndpointCreateDto(BaseModel):
    path: str
    method: EndpointMethodType
    description: Optional[str] = None