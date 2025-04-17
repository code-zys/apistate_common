from typing import Dict
from ..models.user_organisational_unit_ability import UserOrganisationalUnitAbility
from . import BaseMapper

class UserOrganisationalUnitAbilityMapper(BaseMapper):
    @staticmethod
    def to_dict(model: UserOrganisationalUnitAbility) -> Dict:
        """Convert a UserOrganisationalUnitAbility instance to a dictionary.
        
        Args:
            model: The UserOrganisationalUnitAbility instance to convert
            
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

        if 'organisational_unit' in data and data['organisational_unit']:
                data['organisational_unit'] = str(data['organisational_unit'])

        return data