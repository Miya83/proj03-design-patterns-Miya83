from src.patterns.behavioral.strategy import ConcreteStrategyA, ConcreteStrategyB, ConcreteStrategyC, Context

# Test Regular Pricing (no discount)
regular = Context(ConcreteStrategyA())
result1 = regular.do_something([100, 2])
print(f"Regular Pricing: 2 items at $100 each = ${result1[0]}")

# Test Seasonal Pricing (15% off)
seasonal = Context(ConcreteStrategyB())
result2 = seasonal.do_something([100, 2])
print(f"Seasonal Pricing (15% off): 2 items at $100 each = ${result2[0]}")

# Test Clearance Pricing (40% off)
clearance = Context(ConcreteStrategyC())
result3 = clearance.do_something([100, 2])
print(f"Clearance Pricing (40% off): 2 items at $100 each = ${result3[0]}")

# Test changing strategy at runtime
order = Context(ConcreteStrategyA())
print(f"\nRegular: ${order.do_something([50, 3])[0]}")
order.set_strategy(ConcreteStrategyB())
print(f"Seasonal: ${order.do_something([50, 3])[0]}")
order.set_strategy(ConcreteStrategyC())
print(f"Clearance: ${order.do_something([50, 3])[0]}")