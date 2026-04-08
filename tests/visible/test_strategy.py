"""
Visible Tests: Strategy Pattern
CSC3301 Programming Language Paradigms

These tests verify basic Strategy pattern implementation.
Students must implement ConcreteStrategyA and ConcreteStrategyB.
"""
import pytest
from src.patterns.behavioral.strategy import Strategy, Context


class TestStrategyBasics:
    """Basic tests for Strategy pattern - will fail on stub code."""

    def test_concrete_strategy_a_exists(self):
        """ConcreteStrategyA must be implemented."""
        try:
            from src.patterns.behavioral.strategy import ConcreteStrategyA
            strategy = ConcreteStrategyA()
            assert strategy is not None
        except ImportError:
            pytest.fail("ConcreteStrategyA must be implemented")

    def test_concrete_strategy_b_exists(self):
        """ConcreteStrategyB must be implemented."""
        try:
            from src.patterns.behavioral.strategy import ConcreteStrategyB
            strategy = ConcreteStrategyB()
            assert strategy is not None
        except ImportError:
            pytest.fail("ConcreteStrategyB must be implemented")

    def test_strategy_inherits_from_base(self):
        """ConcreteStrategy must inherit from Strategy."""
        try:
            from src.patterns.behavioral.strategy import ConcreteStrategyA
            strategy = ConcreteStrategyA()
            assert isinstance(strategy, Strategy), "Must inherit from Strategy"
        except ImportError:
            pytest.fail("ConcreteStrategyA must be implemented")

    def test_strategy_execute_returns_list(self):
        """Strategy.execute() must return a list."""
        try:
            from src.patterns.behavioral.strategy import ConcreteStrategyA
            strategy = ConcreteStrategyA()
            result = strategy.execute([3, 1, 2])
            assert isinstance(result, list), "execute() should return a list"
        except ImportError:
            pytest.fail("ConcreteStrategyA must be implemented")

    def test_context_uses_strategy(self):
        """Context should use the provided strategy."""
        try:
            from src.patterns.behavioral.strategy import ConcreteStrategyA
            strategy = ConcreteStrategyA()
            context = Context(strategy)
            result = context.do_something([3, 1, 2])
            assert isinstance(result, list), "Context should return strategy result"
        except ImportError:
            pytest.fail("ConcreteStrategyA must be implemented")

    def test_context_can_change_strategy(self):
        """Context should allow changing strategy at runtime."""
        try:
            from src.patterns.behavioral.strategy import ConcreteStrategyA, ConcreteStrategyB

            context = Context(ConcreteStrategyA())
            result1 = context.do_something([3, 1, 2])

            context.set_strategy(ConcreteStrategyB())
            result2 = context.do_something([3, 1, 2])

            # Both should work without errors
            assert isinstance(result1, list)
            assert isinstance(result2, list)
        except ImportError:
            pytest.fail("ConcreteStrategyA and ConcreteStrategyB must be implemented")
