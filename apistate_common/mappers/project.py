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
            if 'organisation' in data and data['organisation']:
                data['organisation'] = str(data['organisation'])
                
            # Handle environment reference
            if 'environment' in data and data['environment']:
                data['environment'] = str(data['environment'])
                
            # Handle organisational_unit reference
            if 'organisational_unit' in data and data['organisational_unit']:
                data['organisational_unit'] = str(data['organisational_unit'])
            
            if 'created_by' in data and data['created_by']:
                data['created_by'] = {
                    'id': str(project.created_by.id),
                    'email': project.created_by.email,
                    'fullname': f"{project.created_by.first_name} {project.created_by.last_name}"
                }
        return data