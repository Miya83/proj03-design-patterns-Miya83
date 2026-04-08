from src.patterns.behavioral.observer import ConcreteSubject, ConcreteObserverA, ConcreteObserverB

# Create order (subject)
order = ConcreteSubject("ORD-001")

# Create observers
customer = ConcreteObserverA()
warehouse = ConcreteObserverB()

# Attach observers
order.attach(customer)
order.attach(warehouse)

# Change status - this will notify all observers
order.status = "Processing"
order.status = "Shipped"
order.status = "Delivered"

# Detach one observer and test again
order.detach(customer)
print("\nAfter detaching customer:")
order.status = "Completed"