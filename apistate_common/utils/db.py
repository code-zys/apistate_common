from typing import Optional, Type, TypeVar, Any
from mongoengine import Document, QuerySet, connect, disconnect
from pydantic import BaseModel

T = TypeVar('T', bound=Document)
M = TypeVar('M', bound=BaseModel)

class DatabaseHandler:
    def __init__(self, db_url: str, db_name: str):
        """
        Initialize database connection
        
        Args:
            db_url: MongoDB connection URL
            db_name: Database name
        """
        self.db_url = db_url
        self.db_name = db_name
        self._connect()
    
    def _connect(self):
        """
        Connect to MongoDB database
        """
        connect(db=self.db_name, host=self.db_url)
    
    def disconnect(self):
        """
        Disconnect from MongoDB database
        """
        disconnect()
    
    def create(self, model: Type[T], data: M) -> T:
        """
        Create a new document
        
        Args:
            model: MongoDB document model class
            data: Pydantic model instance with data
            
        Returns:
            Created document
        """
        document = model(**data.dict())
        return document.save()
    
    def get_by_id(self, model: Type[T], id: str) -> Optional[T]:
        """
        Get document by ID
        
        Args:
            model: MongoDB document model class
            id: Document ID
            
        Returns:
            Document if found, None otherwise
        """
        return model.objects(id=id).first()
    
    def get_by_field(self, model: Type[T], field: str, value: Any) -> Optional[T]:
        """
        Get document by field value
        
        Args:
            model: MongoDB document model class
            field: Field name
            value: Field value
            
        Returns:
            Document if found, None otherwise
        """
        return model.objects(**{field: value}).first()
    
    def update(self, document: T, data: M) -> T:
        """
        Update document with new data
        
        Args:
            document: Document to update
            data: Pydantic model instance with new data
            
        Returns:
            Updated document
        """
        for key, value in data.dict(exclude_unset=True).items():
            setattr(document, key, value)
        return document.save()
    
    def delete(self, document: T) -> bool:
        """
        Delete document
        
        Args:
            document: Document to delete
            
        Returns:
            True if deleted successfully
        """
        document.delete()
        return True
    
    def list_all(self, model: Type[T]) -> QuerySet:
        """
        Get all documents of a model
        
        Args:
            model: MongoDB document model class
            
        Returns:
            QuerySet of all documents
        """
        return model.objects()