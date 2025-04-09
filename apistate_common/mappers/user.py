from typing import Dict, Any
from ..models.user import User
from . import BaseMapper

class UserMapper(BaseMapper):
    @staticmethod
    def to_dict(user: User) -> Dict:
        """Convert a User model instance to a dictionary.
        
        Args:
            user: The User model instance to convert
            
        Returns:
            Dict containing the user data with proper ID handling
        """
        if not user:
            return None
            
        data = BaseMapper.to_dict(user)
        
        # Format specific user fields if needed
        if data:
            # Ensure sensitive fields are not included
            # if 'hashed_password' in data:
            #     del data['hashed_password']
            
            if 'organisation' in data and data['organisation']:
                data['organisation'] = str(data['organisation'])
        return data