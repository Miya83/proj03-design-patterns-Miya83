"""
Adapter Pattern — CSC3301 Project 3: Design Patterns

Allows incompatible interfaces to work together by wrapping
an object in an adapter that translates calls.

TODO: Implement Target, Adaptee, and Adapter classes.
"""
from abc import ABC, abstractmethod


class Target(ABC):
    """The interface that the client expects."""

    @abstractmethod
    def request(self) -> str:
        """Perform the standard request."""
        ...


class Adaptee:
    """The existing class with an incompatible interface.

    Has useful functionality but its interface doesn't match
    what the client code expects.
    """

    def specific_request(self) -> str:
        """Perform the specific (incompatible) request."""
        # TODO: Return a string result
        ...


class Adapter(Target):
    """Adapts the Adaptee interface to the Target interface.

    Wraps an Adaptee and translates Target.request() calls
    into Adaptee.specific_request() calls.
    """

    def __init__(self, adaptee: Adaptee):
        # TODO: Store the adaptee
        ...

    def request(self) -> str:
        # TODO: Delegate to adaptee.specific_request() with translation
        ...
