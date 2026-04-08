"""
Factory Method Pattern
Creates objects without specifying the exact class.
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Product(ABC):
    """Abstract product interface."""
    @abstractmethod
    def operation(self) -> str:
        pass

class Creator(ABC, Generic[T]):
    """Abstract creator with factory method."""
    
    @abstractmethod
    def factory_method(self) -> T:
        """Override in subclasses to create specific products."""
        pass
    
    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: {product.operation()}"

class ShapeFactory:
    """Factory for creating shapes."""

    @staticmethod
    def create(product_type: str):
        """Create a shape based on product_type.

        Args:
            product_type: The type of shape to create (e.g., 'circle', 'square')

        Returns:
            A shape instance
        """
        raise NotImplementedError("ShapeFactory.create() not yet implemented")

# YOUR CODE: Implement ConcreteProductA, ConcreteProductB
# YOUR CODE: Implement ConcreteCreatorA, ConcreteCreatorB
