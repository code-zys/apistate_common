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
            data['project_id'] = str(model.project.id)
        
        if model.organisation:
            data['organisation_id'] = str(model.organisation.id)
        
        if model.connection:
            data['connection_id'] = str(model.connection.id)

        if model.connector:
            data['connector_id'] = str(model.connector.id)

        return APIResponseDto(**data)
