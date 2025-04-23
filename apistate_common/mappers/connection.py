from typing import Optional
from apistate_common.models.connection import Connection
from apistate_common.dtos.connection import ConnectionCreateDTO, ConnectionResponseDTO, ConnectionUpdateDTO
from .base import BaseMapper

class ConnectionMapper(BaseMapper):
    @staticmethod
    def to_response_dto(connection: Connection) -> ConnectionResponseDTO:
        return ConnectionResponseDTO(
            id=str(connection.id),
            name=connection.name,
            connector_id=str(connection.connector.id),
            credential_options=connection.credential_options,
            organisation_unit_id=str(connection.organisation_unit.id) if connection.organisation_unit else None,
            created_at=connection.created_at,
            updated_at=connection.updated_at
        )

    @staticmethod
    def to_model(dto: ConnectionCreateDTO) -> Connection:
        return Connection(
            name=dto.name,
            connector=dto.connector_id,
            credential_options=dto.credential_options,
            organisation_unit=dto.organisation_unit_id
        )

    @staticmethod
    def update_model(connection: Connection, dto: ConnectionUpdateDTO) -> Connection:
        connection.name = dto.name
        connection.connector = dto.connector_id
        connection.credential_options = dto.credential_options
        connection.organisation_unit = dto.organisation_unit_id
        return connection