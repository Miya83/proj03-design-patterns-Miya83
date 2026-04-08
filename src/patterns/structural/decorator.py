"""
Decorator Pattern — CSC3301 Project 3: Design Patterns

Attaches additional responsibilities to an object dynamically.
Provides a flexible alternative to subclassing for extending functionality.

TODO: Implement Component, ConcreteComponent, Decorator, and concrete decorators.
"""
from abc import ABC, abstractmethod


class Component(ABC):
    """Base component interface."""

    @abstractmethod
    def operation(self) -> str:
        """Perform the component's operation."""
        ...


class ConcreteComponent(Component):
    """Default implementation of the component."""

    def operation(self) -> str:
        # TODO: Return base operation result
        ...


class Decorator(Component):
    """Base decorator that wraps a Component.

    Maintains a reference to a Component and delegates calls.
    """

    def __init__(self, component: Component):
        # TODO: Store the wrapped component
        ...

    def operation(self) -> str:
        # TODO: Delegate to wrapped component
        ...


class DecoratorA(Decorator):
    """Adds behavior A to the component."""

    def operation(self) -> str:
        # TODO: Add behavior A around the wrapped component's operation
        ...


class DecoratorB(Decorator):
    """Adds behavior B to the component."""

    def operation(self) -> str:
        # TODO: Add behavior B around the wrapped component's operation
        ...
