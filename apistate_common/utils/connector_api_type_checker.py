from typing import Optional, List, get_type_hints, get_origin, get_args
from pydantic import BaseModel
from functools import wraps
import inspect

class ConnectorAPITypeChecker:
    @staticmethod
    def check_type(value, expected_type) -> bool:
        """
        Check if a value matches the expected type, including support for Lists, Optional types,
        and Pydantic BaseModel instances.
        
        Args:
            value: The value to check
            expected_type: The expected type to check against
            
        Returns:
            bool: True if the value matches the expected type, False otherwise
        """
        origin = get_origin(expected_type)
        args = get_args(expected_type)

        if origin in (list, List):
            return isinstance(value, list) and all(ConnectorAPITypeChecker.check_type(v, args[0]) for v in value)
        if origin is Optional:
            return value is None or ConnectorAPITypeChecker.check_type(value, args[0])
        if inspect.isclass(expected_type) and issubclass(expected_type, BaseModel):
            return isinstance(value, expected_type)
        return isinstance(value, expected_type)

    @staticmethod
    def get_expected_return_type(cls, method_name: str):
        """
        Get the expected return type of a method from its type hints.
        
        Args:
            cls: The class containing the method
            method_name: The name of the method
            
        Returns:
            The expected return type or None if not specified
        """
        method = getattr(cls, method_name)
        return get_type_hints(method).get("return")

    @staticmethod
    def wrap_method(cls, instance, method_name: str):
        """
        Wrap a method to check its return type against the expected type.
        
        Args:
            cls: The class containing the method
            instance: The instance of the class
            method_name: The name of the method to wrap
            
        Returns:
            A wrapped version of the method that includes return type checking
        """
        expected_return_type = ConnectorAPITypeChecker.get_expected_return_type(cls, method_name)
        method = getattr(instance, method_name)

        @wraps(method)
        async def wrapper(*args, **kwargs):
            result = await method(*args, **kwargs)
            if expected_return_type and not ConnectorAPITypeChecker.check_type(result, expected_return_type):
                raise TypeError(f"{method_name}() must return {expected_return_type}, got {type(result)}")
            return result

        return wrapper