from . import BaseMapper
from ..models.connector import Connector
from typing import Dict

class ConnectorMapper(BaseMapper):
    """Mapper for converting Connector models to dictionaries."""
    
    @staticmethod
    def to_dict(model: Connector) -> Dict:
        """Convert a Connector instance to a dictionary.
        
        Args:
            model: The Connector instance to convert
            
        Returns:
            Dict containing the Connector data
        """
        if not model:
            return None
            
        data = BaseMapper.to_dict(model)
        
        # Convert any ObjectId references to strings if needed
        if data and 'organisation' in data and data['organisation']:
            data['organisation'] = str(data['organisation'])
        
        return data