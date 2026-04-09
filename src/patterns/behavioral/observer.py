
"""
Observer Pattern
Notify multiple objects of state changes.
"""
from abc import ABC, abstractmethod
from typing import List, Any

class Subject(ABC):
    """Subject that observers watch."""
    
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
            observer.update(self)

class Observer(ABC):
    """Observer interface."""
    
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = "initial"
    
    def get_state(self):
        return self._state
    
    def set_state(self, state):
        self._state = state
        self.notify()

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverA received update")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverB received update")