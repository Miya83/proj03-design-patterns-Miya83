[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zdJhjHjO)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23455808&assignment_repo_type=AssignmentRepo)
# Project 3: Design Patterns Library

**CSC3301 Programming Language Paradigms**
**Weight:** 5.5% | **Duration:** 3 weeks

## Overview

Design and implement a reusable library demonstrating classic design patterns in Python. Each student receives a unique combination of patterns to implement, ensuring original work while covering the same learning objectives.

## Core Patterns (Required for All)

1. **Factory Method** - Creational pattern that creates objects without specifying the exact class
2. **Observer** - Behavioral pattern that notifies multiple objects of state changes
3. **Strategy** - Behavioral pattern that encapsulates interchangeable algorithms

## Variant Patterns

Check `variant.json` (or `.variant_config.json`) for your 2 additional patterns from:

- **Creational:** Abstract Factory, Builder, Singleton
- **Structural:** Adapter, Decorator, Composite, Facade
- **Behavioral:** Command, State, Template Method

## Requirements

- Each pattern needs abstract base + 2 concrete implementations
- Practical example demonstrating the pattern
- Unit tests with >=90% coverage for each pattern
- UML diagrams in `docs/uml/`

## Milestones

| Milestone | Deliverable | Weight |
|-----------|-------------|--------|
| M1 | Factory Method | 20% |
| M2 | Observer + Strategy | 30% |
| M3 | Variant patterns | 30% |
| Final | Documentation + UML | 20% |

---

## Variant System

This assignment uses a **variant-based system** to generate unique pattern combinations for each student. This ensures academic integrity while maintaining consistent learning objectives.

### How It Works

1. **Automatic Generation**: When your repository is created via GitHub Classroom, a GitHub Action automatically generates your unique variant based on your GitHub username.

2. **Deterministic Hashing**: Your student ID is hashed to deterministically select:
   - 2 additional patterns (beyond the 3 core patterns)
   - A use case domain for implementing patterns

3. **Configuration File**: Your variant is stored in `.variant_config.json`:
   ```json
   {
     "student_id": "your_username",
     "domain": { "name": "E-Commerce Platform", ... },
     "core_patterns": [...],
     "variant_patterns": [...],
     "all_patterns": ["Factory Method", "Observer", "Strategy", "Pattern4", "Pattern5"]
   }
   ```

4. **Personalized Assignment**: After generation, check `ASSIGNMENT.md` for your specific requirements.

### Manual Generation (if needed)

If the automatic generation didn't run, you can generate manually:

```bash
python scripts/variant_generator.py your_student_id
python scripts/generate_assignment.py
```

### Testing with Your Variant

Tests automatically load your variant configuration:

```python
# In tests/visible/conftest.py, fixtures are provided:
def test_pattern(variant_config, variant_patterns):
    # variant_config contains full configuration
    # variant_patterns contains your 2 additional patterns
    pass
```

Run tests:
```bash
pytest tests/visible/ -v
```

### Available Patterns Pool

**Creational Patterns:**
- Abstract Factory - Create families of related objects
- Builder - Construct complex objects step by step
- Singleton - Ensure a class has only one instance

**Structural Patterns:**
- Adapter - Allow incompatible interfaces to work together
- Decorator - Attach additional responsibilities dynamically
- Composite - Compose objects into tree structures
- Facade - Provide a unified interface to a subsystem

**Behavioral Patterns:**
- Command - Encapsulate a request as an object
- State - Alter behavior when internal state changes
- Template Method - Define the skeleton of an algorithm

### Use Case Domains

Your implementation should use examples from your assigned domain:

- E-Commerce Platform
- Game Development
- Document Processing
- Smart Home System
- Banking Application
- Music Streaming
- Restaurant Management
- Healthcare System

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
│       │   └── factory.py
│       ├── structural/
│       │   └── __init__.py
│       └── behavioral/
│           ├── __init__.py
│           ├── observer.py
│           └── strategy.py
├── tests/
│   ├── __init__.py
│   └── visible/
│       ├── __init__.py
│       ├── conftest.py          # Pytest fixtures for variant loading
│       └── test_factory.py
├── scripts/
│   ├── variant_generator.py     # Generates student variant
│   └── generate_assignment.py   # Creates personalized ASSIGNMENT.md
├── docs/
│   └── uml/                     # UML diagrams go here
├── .github/
│   └── workflows/
│       ├── autograding.yml      # Runs tests on push
│       └── generate-variant.yml # Generates variant on repo creation
├── .variant_config.json         # Your unique variant (auto-generated)
├── ASSIGNMENT.md                # Your personalized assignment (auto-generated)
├── ASSIGNMENT_TEMPLATE.md       # Template for assignment generation
├── README.md
└── requirements.txt
```

---

## Getting Started

1. **Check your variant**: Open `.variant_config.json` to see your assigned patterns
2. **Read your assignment**: Open `ASSIGNMENT.md` for detailed requirements
3. **Implement core patterns**: Start with Factory Method in `src/patterns/creational/factory.py`
4. **Add tests**: Write tests in `tests/visible/test_<pattern>.py`
5. **Implement variant patterns**: Complete your 2 additional patterns
6. **Document**: Add UML diagrams and documentation

## Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all visible tests
pytest tests/visible/ -v

# Run with coverage
pytest tests/visible/ --cov=src --cov-report=term-missing
```

## Submission

Push your code to the repository. GitHub Actions will automatically run tests on each push. Check the Actions tab for results.

---

## Resources

- [Refactoring Guru - Design Patterns](https://refactoring.guru/design-patterns)
- [Python Design Patterns](https://python-patterns.guide/)
- [ABC Module Documentation](https://docs.python.org/3/library/abc.html)
