"""
Bridge Pattern — CSC3301 Project 3: Design Patterns

Decouples an abstraction from its implementation so that the two
can vary independently. Useful when you want to avoid permanent binding
between abstraction and implementation.

TODO: Implement Implementor, ConcreteImplementors, Abstraction, and RefinedAbstraction.
"""
from abc import ABC, abstractmethod


class Implementor(ABC):
    """The interface for implementation classes."""

    @abstractmethod
    def operation_impl(self) -> str:
        """Implement the operation."""
        ...


class ConcreteImplementorA(Implementor):
    """Concrete implementation A."""

    def operation_impl(self) -> str:
        """Perform operation using implementation A."""
        # TODO: Return implementation A's result
        ...


class ConcreteImplementorB(Implementor):
    """Concrete implementation B."""

    def operation_impl(self) -> str:
        """Perform operation using implementation B."""
        # TODO: Return implementation B's result
        ...


class Abstraction:
    """The abstract interface that clients use.

    Maintains a reference to an Implementor and delegates work to it.
    """

    def __init__(self, implementor: Implementor):
        # TODO: Store the implementor
        ...

    def operation(self) -> str:
        """Perform the abstracted operation."""
        # TODO: Delegate to the implementor
        ...


class RefinedAbstraction(Abstraction):
    """Extended abstraction that provides additional functionality."""

    def operation(self) -> str:
        """Perform refined operation."""
        # TODO: Extend or enhance the base operation with additional logic
        ...
