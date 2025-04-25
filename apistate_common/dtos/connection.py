from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime
from .base import BaseDTO
from ..enums.connection_status import ConnectionStatus

class ConnectionBaseDTO(BaseDTO):
    id: Optional[str] = None
    name: str
    connector_id: str
    description: Optional[str] = None
    credential_options: Dict
    organisational_unit_id: Optional[str] = None
    last_refresh_date: Optional[int] = None
    expiration_date: Optional[int] = None
    status: ConnectionStatus = ConnectionStatus.NOT_TESTED

class ConnectionCreateDTO(ConnectionBaseDTO):
    pass

class ConnectionUpdateDTO(ConnectionBaseDTO):
    pass

class ConnectionResponseDTO(ConnectionBaseDTO):
    id: str
    created_at: int
    updated_at: int