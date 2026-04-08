"""
Singleton Pattern — CSC3301 Project 3: Design Patterns

Ensures a class has only one instance and provides global access to it.
Must be thread-safe.

TODO: Implement the Singleton class.
"""
import threading
from typing import Optional


class Singleton:
    """Thread-safe Singleton implementation.

    Usage:
        instance = Singleton.get_instance()
        same = Singleton.get_instance()
        assert instance is same
    """
    _instance: Optional['Singleton'] = None
    _lock: threading.Lock = threading.Lock()

    def __init__(self):
        # TODO: Prevent direct instantiation — raise error if instance exists
        ...

    @classmethod
    def get_instance(cls) -> 'Singleton':
        """Return the single instance, creating it if necessary.

        Must be thread-safe using double-checked locking.
        """
        # TODO: Implement thread-safe lazy initialization
        ...
