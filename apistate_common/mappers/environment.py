from typing import Dict, Any
from ..models.environment import Environment
from . import BaseMapper

class EnvironmentMapper(BaseMapper):
    @staticmethod
    def to_dict(environment: Environment) -> Dict:
        """Convert an Environment model instance to a dictionary.
        
        Args:
            environment: The Environment model instance to convert
            
        Returns:
            Dict containing the environment data with proper ID handling
        """
        if not environment:
            return None
            
        data = BaseMapper.to_dict(environment)
        
        if data:
            # Convert timestamps to strings
            if 'created_at' in data:
                data['created_at'] = str(data['created_at'])
            if 'updated_at' in data:
                data['updated_at'] = str(data['updated_at'])
                
            # Handle organization reference
            if 'organisation' in data and data['organisation']:
                data['organisation'] = str(data['organisation'])
                
            # Handle organisational_unit reference
            if 'organisational_unit' in data and data['organisational_unit']:
                data['organisational_unit'] = str(data['organisational_unit'])
            
            if 'created_by' in data and data['created_by']:
                data['created_by'] = {
                    'id': str(environment.created_by.id),
                    'email': environment.created_by.email,
                    'fullname': f"{environment.created_by.lastname} {environment.created_by.firstname}"
                }
        return data