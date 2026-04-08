"""
State Pattern — CSC3301 Project 3: Design Patterns

Allows an object to alter its behavior when its internal state changes.
The object will appear to change its class.

TODO: Implement State, ConcreteStateA, ConcreteStateB, and Context.
"""
from abc import ABC, abstractmethod


class State(ABC):
    """The interface for all concrete states."""

    @abstractmethod
    def handle(self, context: 'Context') -> str:
        """Handle a request in this state."""
        ...


class ConcreteStateA(State):
    """Concrete state A."""

    def handle(self, context: 'Context') -> str:
        """Handle request in state A.

        May transition to state B.
        """
        # TODO: Perform state A behavior and possibly transition states
        ...


class ConcreteStateB(State):
    """Concrete state B."""

    def handle(self, context: 'Context') -> str:
        """Handle request in state B.

        May transition to state A.
        """
        # TODO: Perform state B behavior and possibly transition states
        ...


class Context:
    """The context that maintains an instance of a concrete State.

    Delegates state-specific work to the current state.
    """

    def __init__(self, initial_state: State = None):
        """Initialize context with an initial state."""
        # TODO: Store initial state (or create default state if None)
        ...

    def request(self) -> str:
        """Send a request to the current state."""
        # TODO: Delegate to the current state's handle method
        ...

    def set_state(self, state: State) -> None:
        """Change to a new state."""
        # TODO: Update the current state
        ...
