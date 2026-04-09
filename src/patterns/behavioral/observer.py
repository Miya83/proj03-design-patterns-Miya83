"""
Observer Pattern for E-Commerce Platform.
"""
from abc import ABC, abstractmethod
from typing import List, Any

class Subject(ABC):
    def __init__(self):
        self._observers: List['Observer'] = []
        self._state: Any = None

    def attach(self, observer: 'Observer') -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: 'Observer') -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event: str = None) -> None:
        for observer in self._observers:
            observer.update(event if event else self._state)

class Observer(ABC):
    @abstractmethod
    def update(self, event: str) -> None:
        pass

class ConcreteSubject(Subject):
    def __init__(self, order_id: str = "default"):
        super().__init__()
        self.order_id = order_id
        self._status = "Pending"
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status: str):
        self._status = new_status
        self.notify(new_status)

class ConcreteObserverA(Observer):
    def update(self, event: str) -> None:
        print(f"Customer: Order status is now '{event}'")

class ConcreteObserverB(Observer):
    def update(self, event: str) -> None:
        print(f"Warehouse: Order status updated to '{event}'")
