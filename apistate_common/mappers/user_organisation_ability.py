from typing import Dict
from ..models.user_organisation_ability import UserOrganisationAbility
from . import BaseMapper

class UserOrganisationAbilityMapper(BaseMapper):
    @staticmethod
    def to_dict(model: UserOrganisationAbility) -> Dict:
        """Convert a UserOrganisationAbility instance to a dictionary.
        
        Args:
            model: The UserOrganisationAbility instance to convert
            
        Returns:
            Dict containing the model data with proper ID handling
        """
        if not model:
            return None
            
        data = BaseMapper.to_dict(model)
        
        # Convert user reference to string
        if 'user' in data:
            data['user'] = str(data['user'])
            
        # Convert permissions to list of dictionaries
        if 'permissions' in data:
            data['permissions'] = [BaseMapper.to_dict(perm) for perm in model.permissions]
        
        if 'organisation' in data and data['organisation']:
                data['organisation'] = str(data['organisation'])
        return data