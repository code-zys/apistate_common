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
            if 'password' in data:
                del data['password']
                
            # Convert timestamps to strings if present
            if 'created_at' in data:
                data['created_at'] = str(data['created_at'])
            if 'updated_at' in data:
                data['updated_at'] = str(data['updated_at'])
                
        return data