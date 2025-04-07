from . import BaseMapper
from ..models.organisational_unit import OrganisationalUnit
from typing import Dict

class OrganisationalUnitMapper(BaseMapper):
    """Mapper for converting OrganisationalUnit models to dictionaries."""
    
    @staticmethod
    def to_dict(model: OrganisationalUnit) -> Dict:
        """Convert an OrganisationalUnit instance to a dictionary.
        
        Args:
            model: The OrganisationalUnit instance to convert
            
        Returns:
            Dict containing the OrganisationalUnit data
        """
        if not model:
            return None
            
        data = BaseMapper.to_dict(model)
        
        if data and 'organisation' in data and data['organisation']:
            data['organisation'] = str(data['organisation'])
        
        return data