"""
Pytest configuration and fixtures for Design Patterns tests.
CSC3301 Programming Language Paradigms - Project 3

Loads variant configuration and provides test fixtures with sensible defaults.
"""
import json
import pytest
from pathlib import Path
from typing import Dict, Any, List, Optional


# Default configuration used when no variant config exists
DEFAULT_CONFIG = {
    "student_id": "default_student",
    "hash_seed": 0,
    "domain": {
        "name": "E-Commerce Platform",
        "context": "online shopping system",
        "examples": ["products", "orders", "payments", "shipping"]
    },
    "core_patterns": [
        {
            "name": "Factory Method",
            "module": "factory",
            "category": "creational",
            "description": "Creates objects without specifying the exact class",
            "difficulty": "easy"
        },
        {
            "name": "Observer",
            "module": "observer",
            "category": "behavioral",
            "description": "Notify multiple objects of state changes",
            "difficulty": "medium"
        },
        {
            "name": "Strategy",
            "module": "strategy",
            "category": "behavioral",
            "description": "Encapsulate interchangeable algorithms",
            "difficulty": "easy"
        }
    ],
    "variant_patterns": [
        {
            "name": "Singleton",
            "module": "singleton",
            "category": "creational",
            "description": "Ensure a class has only one instance",
            "difficulty": "easy",
            "domain_context": "online shopping system",
            "requirements": []
        },
        {
            "name": "Adapter",
            "module": "adapter",
            "category": "structural",
            "description": "Allow incompatible interfaces to work together",
            "difficulty": "easy",
            "domain_context": "online shopping system",
            "requirements": []
        }
    ],
    "all_patterns": ["Factory Method", "Observer", "Strategy", "Singleton", "Adapter"],
    "total_patterns": 5,
    "grading": {
        "factory_method": 20,
        "observer": 15,
        "strategy": 15,
        "variant_pattern_1": 15,
        "variant_pattern_2": 15,
        "documentation": 10,
        "uml_diagrams": 10
    }
}


def get_project_root() -> Path:
    """Get the project root directory."""
    # Navigate up from tests/visible/conftest.py to project root
    return Path(__file__).parent.parent.parent


def load_variant_config() -> Dict[str, Any]:
    """
    Load variant configuration from .variant_config.json.
    Returns default config if file doesn't exist.
    """
    config_path = get_project_root() / ".variant_config.json"

    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load variant config: {e}")
            print("Using default configuration.")

    return DEFAULT_CONFIG.copy()


@pytest.fixture(scope="session")
def variant_config() -> Dict[str, Any]:
    """
    Fixture providing the complete variant configuration.

    Usage:
        def test_example(variant_config):
            student_id = variant_config["student_id"]
    """
    return load_variant_config()


@pytest.fixture(scope="session")
def student_id(variant_config: Dict[str, Any]) -> str:
    """Fixture providing the student ID."""
    return variant_config.get("student_id", "default_student")


@pytest.fixture(scope="session")
def domain(variant_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Fixture providing the use case domain.

    Usage:
        def test_domain_context(domain):
            assert domain["name"] in ["E-Commerce Platform", "Game Development", ...]
    """
    return variant_config.get("domain", DEFAULT_CONFIG["domain"])


@pytest.fixture(scope="session")
def core_patterns(variant_config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Fixture providing the list of core patterns (always required).

    Returns list of pattern dicts with: name, module, category, description, difficulty
    """
    return variant_config.get("core_patterns", DEFAULT_CONFIG["core_patterns"])


@pytest.fixture(scope="session")
def variant_patterns(variant_config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Fixture providing the student's variant patterns (2 additional patterns).

    Returns list of pattern dicts with: name, module, category, description,
    difficulty, domain_context, requirements
    """
    return variant_config.get("variant_patterns", DEFAULT_CONFIG["variant_patterns"])


@pytest.fixture(scope="session")
def all_pattern_names(variant_config: Dict[str, Any]) -> List[str]:
    """Fixture providing all pattern names the student must implement."""
    return variant_config.get("all_patterns", DEFAULT_CONFIG["all_patterns"])


@pytest.fixture(scope="session")
def grading_weights(variant_config: Dict[str, Any]) -> Dict[str, int]:
    """Fixture providing the grading weights for each component."""
    return variant_config.get("grading", DEFAULT_CONFIG["grading"])


@pytest.fixture
def pattern_by_name(variant_config: Dict[str, Any]):
    """
    Factory fixture to get pattern info by name.

    Usage:
        def test_pattern(pattern_by_name):
            factory = pattern_by_name("Factory Method")
            assert factory["category"] == "creational"
    """
    all_patterns = (
        variant_config.get("core_patterns", []) +
        variant_config.get("variant_patterns", [])
    )

    def _get_pattern(name: str) -> Optional[Dict[str, Any]]:
        for pattern in all_patterns:
            if pattern["name"] == name:
                return pattern
        return None

    return _get_pattern


@pytest.fixture
def has_pattern(all_pattern_names: List[str]):
    """
    Factory fixture to check if a pattern is required for this variant.

    Usage:
        def test_singleton(has_pattern):
            if has_pattern("Singleton"):
                # Test singleton implementation
    """
    def _has_pattern(name: str) -> bool:
        return name in all_pattern_names

    return _has_pattern


# Test markers for pattern categories
def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "creational: mark test as testing creational patterns"
    )
    config.addinivalue_line(
        "markers", "structural: mark test as testing structural patterns"
    )
    config.addinivalue_line(
        "markers", "behavioral: mark test as testing behavioral patterns"
    )
    config.addinivalue_line(
        "markers", "variant: mark test as variant-specific (may be skipped)"
    )


@pytest.fixture(scope="session")
def src_path() -> Path:
    """Fixture providing the path to the src directory."""
    return get_project_root() / "src"


@pytest.fixture(scope="session")
def patterns_path(src_path: Path) -> Path:
    """Fixture providing the path to the patterns directory."""
    return src_path / "patterns"
