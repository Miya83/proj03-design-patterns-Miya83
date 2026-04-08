"""
Proxy Pattern — CSC3301 Project 3: Design Patterns

Provides a surrogate or placeholder for another object to control access to it.
Useful for lazy initialization, logging, caching, or access control.

TODO: Implement Subject, RealSubject, and Proxy classes.
"""
from abc import ABC, abstractmethod


class Subject(ABC):
    """The interface that both RealSubject and Proxy implement."""

    @abstractmethod
    def request(self) -> str:
        """Process a request."""
        ...


class RealSubject(Subject):
    """The actual object that performs the real work."""

    def request(self) -> str:
        """Perform the actual request."""
        # TODO: Return the actual operation result
        ...


class Proxy(Subject):
    """The proxy that controls access to the RealSubject.

    May implement lazy initialization, logging, caching, or access control.
    """

    def __init__(self):
        # TODO: Initialize with lazy reference to RealSubject (None initially)
        ...

    def request(self) -> str:
        """Control access to the RealSubject.

        May perform additional operations before/after delegating.
        """
        # TODO: Implement access control logic (e.g., lazy initialization)
        ...
