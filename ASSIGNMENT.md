# Project 3: Design Patterns Library

**CSC3301 Programming Language Paradigms**
**Student ID:** patterns
**Weight:** 5.5% | **Duration:** 3 weeks

---

## Your Assignment

Welcome to Project 3! In this project, you will design and implement a reusable library demonstrating classic design patterns in Python. Your implementation should be within the **E-Commerce Platform** domain (online shopping system).

## Required Patterns

You must implement the following **5 design patterns**:

### Core Patterns (Required for All Students)

| Pattern | Category | Module | Points |
|---------|----------|--------|--------|
| Factory Method | Creational | `src/patterns/creational/factory.py` | 20% |
| Observer | Behavioral | `src/patterns/behavioral/observer.py` | 15% |
| Strategy | Behavioral | `src/patterns/behavioral/strategy.py` | 15% |

### Your Variant Patterns

Based on your student ID, you have been assigned these additional patterns:

| Pattern | Category | Module | Points |
|---------|----------|--------|--------|
| {{VARIANT_PATTERN_1_NAME}} | structural | `src/patterns/structural/{{VARIANT_PATTERN_1_MODULE}}.py` | 15% |
| {{VARIANT_PATTERN_2_NAME}} | behavioral | `src/patterns/behavioral/{{VARIANT_PATTERN_2_MODULE}}.py` | 15% |

### Documentation & UML

| Component | Points |
|-----------|--------|
| Documentation | 10% |
| UML Diagrams | 10% |

---

## Domain Context: E-Commerce Platform

Your implementations should use examples from a **online shopping system**. Consider using concepts like:
products, orders, payments, shipping

This will help demonstrate practical applications of the patterns.

---

## Requirements for Each Pattern

For **each** pattern you implement:

1. **Abstract Base Class**
   - Define proper interface using `abc.ABC` and `@abstractmethod`
   - Include type hints for all methods
   - Add docstrings explaining the pattern's purpose

2. **Concrete Implementations**
   - Implement at least **2 concrete classes** per pattern
   - Use domain-relevant examples (online shopping system)
   - Follow Python naming conventions (PEP 8)

3. **Practical Example**
   - Create a working example demonstrating the pattern
   - Include in `examples/` directory or as module docstring

4. **Unit Tests**
   - Achieve **>=90% code coverage** for each pattern
   - Test edge cases and error conditions
   - Place tests in `tests/visible/test_<pattern>.py`

5. **UML Diagram**
   - Create class diagram showing pattern structure
   - Save as `docs/uml/<pattern>_diagram.png` (or PDF/SVG)

---

## Project Structure

```
.
├── src/
│   ├── __init__.py
│   └── patterns/
│       ├── __init__.py
│       ├── creational/
│       │   ├── __init__.py
│       │   ├── factory.py          # Core: Factory Method
│       │   └── {{VARIANT_CREATIONAL_FILES}}
│       ├── structural/
│       │   ├── __init__.py
│       │   └── {{VARIANT_STRUCTURAL_FILES}}
│       └── behavioral/
│           ├── __init__.py
│           ├── observer.py         # Core: Observer
│           ├── strategy.py         # Core: Strategy
│           └── {{VARIANT_BEHAVIORAL_FILES}}
├── tests/
│   └── visible/
│       ├── conftest.py
│       ├── test_factory.py
│       ├── test_observer.py
│       ├── test_strategy.py
│       └── test_{{VARIANT_PATTERN_TESTS}}
├── docs/
│   └── uml/
│       ├── factory_diagram.png
│       └── ...
├── examples/
│   └── ...
├── .variant_config.json
├── README.md
└── requirements.txt
```

---

## Milestones

| Milestone | Deliverable | Weight | Deadline |
|-----------|-------------|--------|----------|
| M1 | Factory Method implementation + tests | 20% | Week 1 |
| M2 | Observer + Strategy implementations + tests | 30% | Week 2 |
| M3 | Variant patterns ({{VARIANT_PATTERN_1_NAME}}, {{VARIANT_PATTERN_2_NAME}}) + tests | 30% | Week 2.5 |
| Final | Documentation + UML diagrams | 20% | Week 3 |

---

## Pattern Descriptions

### Factory Method (Creational)
Creates objects without specifying the exact class. The factory method lets a class defer instantiation to subclasses.

**Your task:** Implement a factory that creates different types of {{DOMAIN_EXAMPLE_1}} based on the request.

### Observer (Behavioral)
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.

**Your task:** Implement a notification system for {{DOMAIN_EXAMPLE_2}} state changes.

### Strategy (Behavioral)
Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

**Your task:** Implement interchangeable algorithms for {{DOMAIN_EXAMPLE_3}} processing.

### {{VARIANT_PATTERN_1_NAME}} (structural)
{{VARIANT_PATTERN_1_DESCRIPTION}}

**Your task:** {{VARIANT_PATTERN_1_TASK}}

### {{VARIANT_PATTERN_2_NAME}} (behavioral)
{{VARIANT_PATTERN_2_DESCRIPTION}}

**Your task:** {{VARIANT_PATTERN_2_TASK}}

---

## Grading Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Correctness | 40% | Patterns work correctly and follow design principles |
| Code Quality | 25% | Clean code, proper typing, documentation |
| Testing | 20% | Comprehensive tests with >=90% coverage |
| Documentation | 15% | Clear README, UML diagrams, docstrings |

---

## Submission

1. Push all code to your GitHub Classroom repository
2. Ensure all tests pass (check GitHub Actions)
3. Submit repository link on Canvas by deadline

**Important:** Your variant patterns are specific to your student ID. Do not copy implementations from classmates as their patterns may differ.

---

## Resources

- [Refactoring Guru - Design Patterns](https://refactoring.guru/design-patterns)
- [Python Design Patterns](https://python-patterns.guide/)
- [ABC Module Documentation](https://docs.python.org/3/library/abc.html)

---

*This assignment was generated specifically for student patterns. Pattern combinations are unique per student.*
