from typing import Dict, Any
from ..models.member import Member
from . import BaseMapper
from .user import UserMapper
from .organisation import OrganizationMapper

class MemberMapper(BaseMapper):
    @staticmethod
    def to_dict(member: Member) -> Dict:
        """Convert a Member model instance to a dictionary.
        
        Args:
            member: The Member model instance to convert
            
        Returns:
            Dict containing the member data with proper ID handling
        """
        if not member:
            return None
            
        data = BaseMapper.to_dict(member)
        
        if data:
            # Handle nested user data
            if hasattr(member, 'user') and member.user:
                data['user'] = UserMapper.to_dict(member.user)
            
            # Handle nested organization data
            if hasattr(member, 'organisation') and member.organisation:
                data['organisation'] = OrganizationMapper.to_dict(member.organisation)
            
            # Ensure type is properly formatted
            if 'type' in data:
                data['type'] = str(data['type'])
                
        return data