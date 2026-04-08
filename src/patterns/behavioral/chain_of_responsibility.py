"""
Chain of Responsibility Pattern — CSC3301 Project 3: Design Patterns

Passes requests along a chain of handlers. Each handler decides either to
process the request or pass it to the next handler in the chain.

TODO: Implement Handler, ConcreteHandlerA, ConcreteHandlerB, and ConcreteHandlerC.
"""
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """The abstract interface for all handlers in the chain."""

    def __init__(self):
        """Initialize the handler."""
        # TODO: Initialize next handler reference to None
        ...

    def set_next(self, handler: 'Handler') -> 'Handler':
        """Set the next handler in the chain.

        Returns self for chaining.
        """
        # TODO: Store next handler and return self
        ...

    @abstractmethod
    def handle(self, request: str) -> str:
        """Handle the request or pass it to the next handler."""
        ...


class ConcreteHandlerA(Handler):
    """Concrete handler A in the chain."""

    def handle(self, request: str) -> str:
        """Handle or pass the request.

        Handler A handles certain requests and passes others.
        """
        # TODO: Check if this handler can handle the request.
        # If yes, handle it and return result.
        # If no, pass to next handler (if available).
        ...


class ConcreteHandlerB(Handler):
    """Concrete handler B in the chain."""

    def handle(self, request: str) -> str:
        """Handle or pass the request.

        Handler B handles certain requests and passes others.
        """
        # TODO: Check if this handler can handle the request.
        # If yes, handle it and return result.
        # If no, pass to next handler (if available).
        ...


class ConcreteHandlerC(Handler):
    """Concrete handler C in the chain."""

    def handle(self, request: str) -> str:
        """Handle or pass the request.

        Handler C handles certain requests and passes others.
        """
        # TODO: Check if this handler can handle the request.
        # If yes, handle it and return result.
        # If no, pass to next handler (if available).
        ...
