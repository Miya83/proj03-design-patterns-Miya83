#!/usr/bin/env python3
"""
Variant Generator for Design Patterns Assignment
CSC3301 Programming Language Paradigms - Project 3

Generates unique assignment variants based on student ID hash.
Selects 2 additional patterns and assigns use case domains.
"""
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, List, Any


# Available additional patterns (beyond core: Factory Method, Observer, Strategy)
ADDITIONAL_PATTERNS = {
    "creational": [
        {
            "name": "Abstract Factory",
            "module": "abstract_factory",
            "description": "Provide an interface for creating families of related objects",
            "difficulty": "medium"
        },
        {
            "name": "Builder",
            "module": "builder",
            "description": "Construct complex objects step by step",
            "difficulty": "medium"
        },
        {
            "name": "Singleton",
            "module": "singleton",
            "description": "Ensure a class has only one instance",
            "difficulty": "easy"
        }
    ],
    "structural": [
        {
            "name": "Adapter",
            "module": "adapter",
            "description": "Allow incompatible interfaces to work together",
            "difficulty": "easy"
        },
        {
            "name": "Decorator",
            "module": "decorator",
            "description": "Attach additional responsibilities dynamically",
            "difficulty": "medium"
        },
        {
            "name": "Composite",
            "module": "composite",
            "description": "Compose objects into tree structures",
            "difficulty": "medium"
        },
        {
            "name": "Facade",
            "module": "facade",
            "description": "Provide a unified interface to a subsystem",
            "difficulty": "easy"
        }
    ],
    "behavioral": [
        {
            "name": "Command",
            "module": "command",
            "description": "Encapsulate a request as an object",
            "difficulty": "medium"
        },
        {
            "name": "State",
            "module": "state",
            "description": "Alter behavior when internal state changes",
            "difficulty": "medium"
        },
        {
            "name": "Template Method",
            "module": "template_method",
            "description": "Define the skeleton of an algorithm",
            "difficulty": "easy"
        }
    ]
}

# Use case domains for pattern implementation
USE_CASE_DOMAINS = [
    {
        "name": "E-Commerce Platform",
        "context": "online shopping system",
        "examples": ["products", "orders", "payments", "shipping"]
    },
    {
        "name": "Game Development",
        "context": "video game engine",
        "examples": ["characters", "weapons", "levels", "inventory"]
    },
    {
        "name": "Document Processing",
        "context": "document management system",
        "examples": ["documents", "formats", "converters", "templates"]
    },
    {
        "name": "Smart Home System",
        "context": "IoT home automation",
        "examples": ["devices", "sensors", "commands", "schedules"]
    },
    {
        "name": "Banking Application",
        "context": "financial services platform",
        "examples": ["accounts", "transactions", "reports", "notifications"]
    },
    {
        "name": "Music Streaming",
        "context": "audio streaming service",
        "examples": ["tracks", "playlists", "recommendations", "playback"]
    },
    {
        "name": "Restaurant Management",
        "context": "food service system",
        "examples": ["menu items", "orders", "kitchen", "billing"]
    },
    {
        "name": "Healthcare System",
        "context": "medical records platform",
        "examples": ["patients", "appointments", "prescriptions", "reports"]
    }
]


def generate_hash(student_id: str) -> int:
    """Generate a deterministic hash from student ID."""
    hash_bytes = hashlib.sha256(student_id.encode()).digest()
    return int.from_bytes(hash_bytes[:8], byteorder='big')


def select_patterns(hash_value: int) -> List[Dict[str, Any]]:
    """
    Select 2 additional patterns based on hash.
    Ensures diversity by selecting from different categories when possible.
    """
    # Flatten all patterns with their category
    all_patterns = []
    for category, patterns in ADDITIONAL_PATTERNS.items():
        for pattern in patterns:
            all_patterns.append({**pattern, "category": category})

    # Use hash to select patterns
    num_patterns = len(all_patterns)

    # First pattern selection
    first_idx = hash_value % num_patterns
    first_pattern = all_patterns[first_idx]

    # Second pattern selection (ensure it's different and preferably from different category)
    remaining_patterns = [
        p for i, p in enumerate(all_patterns)
        if i != first_idx
    ]

    # Prefer different category
    different_category = [
        p for p in remaining_patterns
        if p["category"] != first_pattern["category"]
    ]

    if different_category:
        second_idx = (hash_value // num_patterns) % len(different_category)
        second_pattern = different_category[second_idx]
    else:
        second_idx = (hash_value // num_patterns) % len(remaining_patterns)
        second_pattern = remaining_patterns[second_idx]

    return [first_pattern, second_pattern]


def select_domain(hash_value: int) -> Dict[str, Any]:
    """Select a use case domain based on hash."""
    domain_idx = (hash_value // 1000) % len(USE_CASE_DOMAINS)
    return USE_CASE_DOMAINS[domain_idx]


def generate_pattern_requirements(pattern: Dict[str, Any], domain: Dict[str, Any]) -> Dict[str, Any]:
    """Generate specific requirements for a pattern within the domain context."""
    return {
        "name": pattern["name"],
        "module": pattern["module"],
        "category": pattern["category"],
        "description": pattern["description"],
        "difficulty": pattern["difficulty"],
        "domain_context": domain["context"],
        "requirements": [
            f"Implement {pattern['name']} pattern using {domain['context']} examples",
            "Create abstract base class with proper interface",
            "Implement at least 2 concrete classes",
            "Include comprehensive unit tests (>=90% coverage)",
            "Add UML class diagram in docs/uml/"
        ]
    }


def generate_variant(student_id: str) -> Dict[str, Any]:
    """Generate complete variant configuration for a student."""
    hash_value = generate_hash(student_id)

    # Select patterns and domain
    selected_patterns = select_patterns(hash_value)
    domain = select_domain(hash_value)

    # Generate pattern requirements
    pattern_requirements = [
        generate_pattern_requirements(p, domain)
        for p in selected_patterns
    ]

    # Core patterns (always required)
    core_patterns = [
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
    ]

    return {
        "student_id": student_id,
        "hash_seed": hash_value,
        "domain": domain,
        "core_patterns": core_patterns,
        "variant_patterns": pattern_requirements,
        "all_patterns": [p["name"] for p in core_patterns] + [p["name"] for p in pattern_requirements],
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


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python variant_generator.py <student_id>")
        print("Example: python variant_generator.py john_doe")
        sys.exit(1)

    student_id = sys.argv[1]

    # Generate variant
    variant = generate_variant(student_id)

    # Save to config file
    repo_root = Path(__file__).parent.parent
    config_path = repo_root / ".variant_config.json"

    with open(config_path, 'w') as f:
        json.dump(variant, f, indent=2)

    print(f"Generated variant for student: {student_id}")
    print(f"Domain: {variant['domain']['name']}")
    print(f"Variant patterns:")
    for p in variant['variant_patterns']:
        print(f"  - {p['name']} ({p['category']})")
    print(f"Config saved to: {config_path}")


if __name__ == "__main__":
    main()
