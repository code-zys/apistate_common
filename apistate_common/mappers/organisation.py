from typing import Dict, Any
from ..models.organisation import Organisation
from . import BaseMapper

class OrganisationMapper(BaseMapper):
    @staticmethod
    def to_dict(organization: Organisation) -> Dict:
        """Convert an Organization model instance to a dictionary.
        
        Args:
            organization: The Organization model instance to convert
            
        Returns:
            Dict containing the organization data with proper ID handling
        """
        if not organization:
            return None
            
        data = BaseMapper.to_dict(organization)
        
        if data:
            # Convert timestamps to strings
            if 'created_at' in data:
                data['created_at'] = str(data['created_at'])
            if 'updated_at' in data:
                data['updated_at'] = str(data['updated_at'])
                
            # Handle any nested relationships if needed
            if 'parent' in data and data['parent']:
                data['parent'] = str(data['parent'])
                
        return data