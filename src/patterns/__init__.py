"""CSC3301 Design Patterns Library."""

# Creational patterns
try:
    from .creational import Singleton
except ImportError:
    pass

try:
    from .creational import ShapeFactory
except ImportError:
    pass

# Structural patterns
try:
    from .structural import (
        Adapter, Target, Adaptee,
        Decorator, Component, ConcreteComponent, DecoratorA, DecoratorB,
        Proxy, RealSubject,
        Implementor, ConcreteImplementorA, ConcreteImplementorB, Abstraction, RefinedAbstraction,
    )
except ImportError:
    pass

# Behavioral patterns
try:
    from .behavioral import (
        AbstractClass, ConcreteClassA, ConcreteClassB,
        Command, ConcreteCommand, Receiver, Invoker,
        State, ConcreteStateA, ConcreteStateB,
        Handler, ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC,
    )
except ImportError:
    pass

# Observer pattern
try:
    from .behavioral import Observer, Subject
except ImportError:
    pass

# Strategy pattern
try:
    from .behavioral import ConcreteStrategyA, ConcreteStrategyB, Context
except ImportError:
    pass

__all__ = [
    # Creational
    'Singleton',
    'ShapeFactory',
    # Structural - Adapter
    'Adapter',
    'Target',
    'Adaptee',
    # Structural - Decorator
    'Decorator',
    'Component',
    'ConcreteComponent',
    'DecoratorA',
    'DecoratorB',
    # Structural - Proxy
    'Proxy',
    'RealSubject',
    # Structural - Bridge
    'Implementor',
    'ConcreteImplementorA',
    'ConcreteImplementorB',
    'Abstraction',
    'RefinedAbstraction',
    # Behavioral - Template Method
    'AbstractClass',
    'ConcreteClassA',
    'ConcreteClassB',
    # Behavioral - Command
    'Command',
    'ConcreteCommand',
    'Receiver',
    'Invoker',
    # Behavioral - State
    'State',
    'ConcreteStateA',
    'ConcreteStateB',
    'Context',
    # Behavioral - Chain of Responsibility
    'Handler',
    'ConcreteHandlerA',
    'ConcreteHandlerB',
    'ConcreteHandlerC',
    # Behavioral - Observer
    'Observer',
    'Subject',
    # Behavioral - Strategy
    'ConcreteStrategyA',
    'ConcreteStrategyB',
]
