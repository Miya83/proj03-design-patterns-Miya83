"""Behavioral patterns."""
from .template_method import AbstractClass, ConcreteClassA, ConcreteClassB
from .command import Command, ConcreteCommand, Receiver, Invoker
from .state import State, ConcreteStateA, ConcreteStateB, Context
from .chain_of_responsibility import Handler, ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC
from .observer import Observer, Subject
from .strategy import ConcreteStrategyA, ConcreteStrategyB

__all__ = [
    # Template Method
    'AbstractClass',
    'ConcreteClassA',
    'ConcreteClassB',
    # Command
    'Command',
    'ConcreteCommand',
    'Receiver',
    'Invoker',
    # State
    'State',
    'ConcreteStateA',
    'ConcreteStateB',
    'Context',
    # Chain of Responsibility
    'Handler',
    'ConcreteHandlerA',
    'ConcreteHandlerB',
    'ConcreteHandlerC',
    # Observer
    'Observer',
    'Subject',
    # Strategy
    'ConcreteStrategyA',
    'ConcreteStrategyB',
]
