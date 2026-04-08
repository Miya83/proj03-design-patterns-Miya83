"""Structural patterns."""
from .adapter import Adapter, Target, Adaptee
from .decorator import Decorator, Component, ConcreteComponent, DecoratorA, DecoratorB
from .proxy import Proxy, Subject, RealSubject
from .bridge import Implementor, ConcreteImplementorA, ConcreteImplementorB, Abstraction, RefinedAbstraction

__all__ = [
    # Adapter
    'Adapter',
    'Target',
    'Adaptee',
    # Decorator
    'Decorator',
    'Component',
    'ConcreteComponent',
    'DecoratorA',
    'DecoratorB',
    # Proxy
    'Proxy',
    'Subject',
    'RealSubject',
    # Bridge
    'Implementor',
    'ConcreteImplementorA',
    'ConcreteImplementorB',
    'Abstraction',
    'RefinedAbstraction',
]
