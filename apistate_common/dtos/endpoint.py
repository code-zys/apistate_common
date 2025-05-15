from typing import Optional
from pydantic import BaseModel

class EndpointCreateDto(BaseModel):
    path: str
    method: str
    description: Optional[str] = None