
"""
Strategy Pattern for E-Commerce Platform.
"""
from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):
    @abstractmethod
    def execute(self, data: List[int]) -> List[int]:
        pass

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, data: List[int]) -> List[int]:
        return self._strategy.execute(data)

    def do_something(self, data: List[int]) -> List[int]:
        return self.execute_strategy(data)

class ConcreteStrategyA(Strategy):
    def execute(self, data: List[int]) -> List[int]:
        # Regular pricing - no discount
        price = data[0]
        quantity = data[1]
        return [price * quantity]

class ConcreteStrategyB(Strategy):
    def execute(self, data: List[int]) -> List[int]:
        # Seasonal pricing - 15% discount
        price = data[0]
        quantity = data[1]
        return [int((price * quantity) * 0.85)]