"""
Template Method Pattern — CSC3301 Project 3: Design Patterns

Defines the skeleton of an algorithm in a base class,
letting subclasses override specific steps without changing the algorithm's structure.

TODO: Implement AbstractClass, ConcreteClassA, and ConcreteClassB.
"""
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """Abstract class that defines the template method."""

    def template_method(self) -> str:
        """The template method defines the structure of the algorithm.

        This method is final and should not be overridden.
        """
        # TODO: Call primitive operations in a defined sequence
        # and combine results into a final string
        ...

    @abstractmethod
    def primitive_operation_a(self) -> str:
        """First primitive operation to be implemented by subclasses."""
        ...

    @abstractmethod
    def primitive_operation_b(self) -> str:
        """Second primitive operation to be implemented by subclasses."""
        ...


class ConcreteClassA(AbstractClass):
    """Concrete implementation A of the template method."""

    def primitive_operation_a(self) -> str:
        """Implement operation A for class A."""
        # TODO: Return concrete implementation A's result
        ...

    def primitive_operation_b(self) -> str:
        """Implement operation B for class A."""
        # TODO: Return concrete implementation B's result
        ...


class ConcreteClassB(AbstractClass):
    """Concrete implementation B of the template method."""

    def primitive_operation_a(self) -> str:
        """Implement operation A for class B."""
        # TODO: Return concrete implementation A's result
        ...

    def primitive_operation_b(self) -> str:
        """Implement operation B for class B."""
        # TODO: Return concrete implementation B's result
        ...
