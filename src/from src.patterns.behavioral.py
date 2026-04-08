from src.patterns.behavioral.template_method import ConcreteClassA, ConcreteClassB

standard = ConcreteClassA()
print(standard.template_method("ORD-001", "John", 100))

express = ConcreteClassB()
print(express.template_method("ORD-002", "Jane", 100))