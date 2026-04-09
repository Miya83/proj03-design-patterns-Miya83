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

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Processing payment via Credit Card"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Processing payment via PayPal"

class ConcreteCreatorA(Creator[ConcreteProductA]):
    def factory_method(self) -> ConcreteProductA:
        return ConcreteProductA()

class ConcreteCreatorB(Creator[ConcreteProductB]):
    def factory_method(self) -> ConcreteProductB:
        return ConcreteProductB()

class ShapeFactory:
    @staticmethod
    def create(product_type: str):
        if product_type.lower() == "creditcard":
            return ConcreteProductA()
        elif product_type.lower() == "paypal":
            return ConcreteProductB()
        else:
            raise ValueError(f"Unknown payment type: {product_type}")