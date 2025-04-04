from typing import Dict, Any, Union
from datetime import datetime
from bson import ObjectId
from mongoengine import Document, EmbeddedDocument

class BaseMapper:
    @staticmethod
    def to_dict(model: Union[Document, EmbeddedDocument]) -> Dict:
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
            
        # Handle common fields from BaseDocument
        for field in ['created_at', 'updated_at', 'deleted_at']:
            if field in data:
                data[field] = str(data[field])
                
        # Handle reference fields
        for field in ['created_by', 'updated_by', 'deleted_by']:
            if field in data and data[field]:
                data[field] = str(data[field])
                
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