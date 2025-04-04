from typing import Dict, Any
from ..models.project import Project
from . import BaseMapper

class ProjectMapper(BaseMapper):
    @staticmethod
    def to_dict(project: Project) -> Dict:
        """Convert a Project model instance to a dictionary.
        
        Args:
            project: The Project model instance to convert
            
        Returns:
            Dict containing the project data with proper ID handling
        """
        if not project:
            return None
            
        data = BaseMapper.to_dict(project)
        
        if data:
            # Convert timestamps to strings
            if 'created_at' in data:
                data['created_at'] = str(data['created_at'])
            if 'updated_at' in data:
                data['updated_at'] = str(data['updated_at'])
                
            # Handle organization reference
            if 'organization' in data and data['organization']:
                data['organization'] = str(data['organization'])
                
            # Handle environment references
            if 'environments' in data and data['environments']:
                data['environments'] = [str(env_id) for env_id in data['environments']]
                
        return data