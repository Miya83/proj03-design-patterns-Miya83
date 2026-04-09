"""
Strategy Pattern
Encapsulate interchangeable algorithms.
"""
from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):
    """Strategy interface."""
    
    @abstractmethod
    def execute(self, data: List[int]) -> List[int]:
        pass

class Context:
    """Context uses a Strategy."""
    
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def execute_strategy(self, data: List[int]) -> List[int]:
        return self._strategy.execute(data)
    
    def do_something(self, data: List[int]) -> List[int]:
        """Alias for execute_strategy (used by visible tests)."""
        return self.execute_strategy(data)

class ConcreteStrategyA(Strategy):
    """Concrete strategy A - sorts ascending."""
    
    def execute(self, data: List[int]) -> List[int]:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    """Concrete strategy B - sorts descending."""
    
    def execute(self, data: List[int]) -> List[int]:
        return sorted(data, reverse=True)