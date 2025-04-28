from ..models.api import API
from ..dtos.api import APIResponseDto
from . import BaseMapper

class APIMapper(BaseMapper):
    """Mapper for API model and DTOs."""
    @classmethod
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

        return APIResponseDto(**data)