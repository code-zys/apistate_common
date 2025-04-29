from bson import ObjectId
from ..models.api import API
from ..dtos.api import APICreateDto, APIUpdateDto, APIResponseDto
from . import BaseMapper

class APIMapper(BaseMapper):
    """Mapper for API model and DTOs."""
    @staticmethod
    def to_dict(model: API) -> APIResponseDto:
        """Convert API model to DTO.
        
        Args:
            model: API model instance
            
        Returns:
            APIResponseDto instance
        """
        if not model:
            return None
            
        data = BaseMapper.to_dict(model)

        if model.project:
            data['project'] = str(model.project.id)
        
        if model.organisation:
            data['organisation'] = str(model.organisation.id)

        return APIResponseDto(**data)


class APIMapper:
    """Mapper for transforming between API models and DTOs."""
    
    @staticmethod
    def to_model(dto: APICreateDto, organisation_id: str) -> API:
        """Convert create DTO to API model."""
        return API(
            name=dto.name,
            description=dto.description,
            version=dto.version,
            project=ObjectId(dto.project_id),
            connection=ObjectId(dto.connection_id),
            connector=ObjectId(dto.connector_id),
            status=dto.status,
            organisation=ObjectId(organisation_id)
        )

    @staticmethod
    def to_response_dto(api: API) -> APIResponseDto:
        """Convert API model to response DTO."""
        return APIResponseDto(
            id=str(api.id),
            name=api.name,
            description=api.description,
            version=api.version,
            project_id=str(api.project.id) if api.project else None,
            connection_id=str(api.connection.id),
            connector_id=str(api.connector.id),
            status=api.status,
            organisation_id=str(api.organisation.id)
        )

    @staticmethod
    def update_model(api: API, dto: APIUpdateDto) -> API:
        """Update API model with DTO data."""
        if dto.name is not None:
            api.name = dto.name
        if dto.description is not None:
            api.description = dto.description
        if dto.version is not None:
            api.version = dto.version
        if dto.project_id is not None:
            api.project = ObjectId(dto.project_id)
        if dto.connection_id is not None:
            api.connection = ObjectId(dto.connection_id)
        if dto.connector_id is not None:
            api.connector = ObjectId(dto.connector_id)
        if dto.status is not None:
            api.status = dto.status
        return api