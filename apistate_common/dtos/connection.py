from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime
from .base import BaseDTO

class ConnectionBaseDTO(BaseDTO):
    name: str
    connector_id: str
    description: str
    credential_options: Dict
    organisation_unit_id: Optional[str] = None

class ConnectionCreateDTO(ConnectionBaseDTO):
    pass

class ConnectionUpdateDTO(ConnectionBaseDTO):
    pass

class ConnectionResponseDTO(ConnectionBaseDTO):
    id: str
    created_at: datetime
    updated_at: Optional[datetime]