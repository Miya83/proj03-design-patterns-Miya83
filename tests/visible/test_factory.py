"""
Visible Tests: Factory Method Pattern
CSC3301 Programming Language Paradigms

These tests verify basic Factory pattern implementation.
Students must implement ConcreteProductA, ConcreteProductB,
ConcreteCreatorA, and ConcreteCreatorB.
"""
import pytest
from src.patterns.creational.factory import Creator, Product


class TestFactoryBasics:
    """Basic tests for Factory pattern - will fail on stub code."""

    def test_concrete_product_exists(self):
        """ConcreteProductA must be implemented."""
        from src.patterns.creational.factory import ConcreteProductA

        product = ConcreteProductA()
        assert product is not None, "ConcreteProductA should be instantiable"

    def test_concrete_product_has_operation(self):
        """ConcreteProduct must implement operation()."""
        from src.patterns.creational.factory import ConcreteProductA

        product = ConcreteProductA()
        result = product.operation()
        assert isinstance(result, str), "operation() should return a string"
        assert len(result) > 0, "operation() should return non-empty string"

    def test_product_is_product_subclass(self):
        """ConcreteProduct must inherit from Product."""
        from src.patterns.creational.factory import ConcreteProductA

        product = ConcreteProductA()
        assert isinstance(product, Product), "ConcreteProductA must inherit from Product"

    def test_concrete_creator_exists(self):
        """ConcreteCreatorA must be implemented."""
        from src.patterns.creational.factory import ConcreteCreatorA

        creator = ConcreteCreatorA()
        assert creator is not None, "ConcreteCreatorA should be instantiable"

    def test_creator_factory_method(self):
        """Creator.factory_method() must return a Product."""
        from src.patterns.creational.factory import ConcreteCreatorA

        creator = ConcreteCreatorA()
        product = creator.factory_method()
        assert product is not None, "factory_method() should return a product"
        assert isinstance(product, Product), "factory_method() should return a Product"

    def test_creator_some_operation(self):
        """Creator.some_operation() should use the product."""
        from src.patterns.creational.factory import ConcreteCreatorA

        creator = ConcreteCreatorA()
        result = creator.some_operation()
        assert isinstance(result, str), "some_operation() should return a string"
        assert "Creator:" in result, "some_operation() should format result correctly"
