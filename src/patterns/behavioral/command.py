"""
Command Pattern — CSC3301 Project 3: Design Patterns

Encapsulates a request as an object, allowing you to parameterize clients
with different requests, queue requests, and support undoable operations.

TODO: Implement Command, ConcreteCommand, Receiver, and Invoker.
"""
from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    """The interface for all commands."""

    @abstractmethod
    def execute(self) -> str:
        """Execute the command."""
        ...


class Receiver:
    """The object that knows how to perform the actual work."""

    def action_a(self) -> str:
        """Perform action A."""
        # TODO: Return result of action A
        ...

    def action_b(self) -> str:
        """Perform action B."""
        # TODO: Return result of action B
        ...


class ConcreteCommand(Command):
    """Concrete command that binds a Receiver with an action."""

    def __init__(self, receiver: Receiver, action: str = 'a'):
        """Initialize command with a receiver and action type.

        Args:
            receiver: The Receiver object to perform the action.
            action: Type of action ('a' or 'b').
        """
        # TODO: Store receiver and action
        ...

    def execute(self) -> str:
        """Execute the command by calling the receiver's action."""
        # TODO: Call the appropriate action on the receiver
        ...


class Invoker:
    """The object that invokes commands.

    May store, queue, or manage commands.
    """

    def __init__(self):
        """Initialize the invoker."""
        # TODO: Initialize a list to store commands
        ...

    def store_command(self, command: Command) -> None:
        """Store a command for later execution."""
        # TODO: Add command to the list
        ...

    def execute_command(self, command: Command) -> str:
        """Execute a single command immediately."""
        # TODO: Execute and return result of the command
        ...

    def execute_all(self) -> str:
        """Execute all stored commands in order."""
        # TODO: Execute all stored commands and return combined results
        ...
