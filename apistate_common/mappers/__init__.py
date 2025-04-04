from typing import Dict, Any
from bson import ObjectId

class BaseMapper:
    @staticmethod
    def to_dict(model: Any) -> Dict:
        """Convert a model instance to a dictionary.
        
        Args:
            model: The model instance to convert
            
        Returns:
            Dict containing the model data with proper ID handling
        """
        if not model:
            return None
            
        data = model.to_mongo().to_dict()
        
        # Convert _id to string id
        if '_id' in data:
            data['id'] = str(data['_id'])
            del data['_id']
            
        return data
    
    @staticmethod
    def convert_object_id(value: Any) -> Any:
        """Convert ObjectId to string if present.
        
        Args:
            value: The value to check and potentially convert
            
        Returns:
            String if value is ObjectId, otherwise original value
        """
        if isinstance(value, ObjectId):
            return str(value)
        return value