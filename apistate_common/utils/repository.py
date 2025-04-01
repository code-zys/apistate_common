from typing import TypeVar, Generic, List, Optional, Type
from mongoengine import Document, QuerySet
from mongoengine.errors import ValidationError, DoesNotExist

T = TypeVar('T', bound=Document)

class BaseRepository(Generic[T]):
    """Generic base repository for MongoDB operations.
    
    Provides common database operations that can be reused across repositories.
    """
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    def find_by_id(self, id: str) -> Optional[T]:
        """Find a document by its ID."""
        try:
            return self.model_class.objects.get(id=id)
        except (ValidationError, DoesNotExist):
            return None

    def find_all(self) -> QuerySet:
        """Get all documents."""
        return self.model_class.objects.all()

    def create(self, **kwargs) -> T:
        """Create a new document."""
        instance = self.model_class(**kwargs)
        instance.save()
        return instance

    def update(self, instance: T, **kwargs) -> T:
        """Update an existing document."""
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, instance: T) -> bool:
        """Delete a document."""
        try:
            instance.delete()
            return True
        except Exception:
            return False