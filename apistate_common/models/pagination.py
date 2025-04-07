from typing import TypeVar, Generic, List
from pydantic import BaseModel

T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response model.
    
    Args:
        T: The type of items in the data field.
    
    Attributes:
        data: List of items of type T.
        total_items: Total number of items across all pages.
        total_pages: Total number of pages.
        current_page: Current page number.
        page_size: Number of items per page.
        has_next: Whether there is a next page.
        has_previous: Whether there is a previous page.
    """
    data: List[T]
    total_items: int
    total_pages: int
    current_page: int
    page_size: int
    has_next: bool
    has_previous: bool

    @classmethod
    def create(cls, items: List[T], total_items: int, page: int, page_size: int) -> 'PaginatedResponse[T]':
        """Create a paginated response.
        
        Args:
            items: List of items for the current page.
            total_items: Total number of items across all pages.
            page: Current page number.
            page_size: Number of items per page.
        
        Returns:
            A PaginatedResponse instance.
        """
        total_pages = (total_items + page_size - 1) // page_size if total_items > 0 else 0
        
        return cls(
            data=items,
            total_items=total_items,
            total_pages=total_pages,
            current_page=page,
            page_size=page_size,
            has_next=page < total_pages,
            has_previous=page > 1
        )