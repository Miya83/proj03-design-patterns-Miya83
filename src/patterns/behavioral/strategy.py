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
    """Concrete strategy A."""

    def execute(self, data: List[int]) -> List[int]:
        raise NotImplementedError("ConcreteStrategyA.execute() not yet implemented")

class ConcreteStrategyB(Strategy):
    """Concrete strategy B."""

    def execute(self, data: List[int]) -> List[int]:
        raise NotImplementedError("ConcreteStrategyB.execute() not yet implemented")

# YOUR CODE: Implement ConcreteStrategyA (e.g., BubbleSort)
# YOUR CODE: Implement ConcreteStrategyB (e.g., QuickSort)
