from typing import Optional, Dict
from apistate_common.models.connection import Connection
from apistate_common.dtos.connection import ConnectionCreateDTO, ConnectionResponseDTO, ConnectionUpdateDTO
from . import BaseMapper
import json

class ConnectionMapper(BaseMapper):
    @staticmethod
    def to_response_dto(connection: Connection) -> ConnectionResponseDTO:
        # Credential options are already decrypted by the service layer
        credential_options = json.loads(connection.credential_options) if isinstance(connection.credential_options, str) else connection.credential_options
        return ConnectionResponseDTO(
            id=str(connection.id),
            name=connection.name,
            description=connection.description,
            connector_id=str(connection.connector.id),
            credential_options=credential_options,
            organisational_unit_id=str(connection.organisational_unit.id) if connection.organisational_unit else None,
            created_at=connection.created_at,
            updated_at=connection.updated_at,
            status=connection.status,
            last_refresh_date=connection.last_refresh_date,
            expiration_date=connection.expiration_date
        )

    @staticmethod
    def to_model(dto: ConnectionCreateDTO) -> Connection:
        # Convert dict to string for storage, encryption handled by service layer
        credential_options = json.dumps(dto.credential_options) if isinstance(dto.credential_options, dict) else dto.credential_options
        return Connection(
            id=dto.id,
            name=dto.name,
            connector=dto.connector_id,
            description=dto.description,
            credential_options=credential_options,
            organisational_unit=dto.organisational_unit_id,
            status=dto.status.value,
            last_refresh_date=dto.last_refresh_date,
            expiration_date=dto.expiration_date
        )

    @staticmethod
    def update_model(connection: Connection, dto: ConnectionUpdateDTO) -> Connection:
        # Convert dict to string for storage, encryption handled by service layer
        credential_options = json.dumps(dto.credential_options) if isinstance(dto.credential_options, dict) else dto.credential_options
        connection.name = dto.name
        connection.connector = dto.connector_id
        connection.description = dto.description
        connection.credential_options = credential_options
        connection.organisational_unit = dto.organisational_unit_id
        connection.status = dto.status
        connection.last_refresh_date = dto.last_refresh_date
        connection.expiration_date = dto.expiration_date
        return connection