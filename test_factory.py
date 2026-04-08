from src.patterns.creational.factory import (
    CreditCardFactory, PayPalFactory, CryptoFactory, ShapeFactory
)

print("Testing Factory Method Pattern - Payment Processing")
print("=" * 50)

# Test using Concrete Factories
print("\n--- Using Concrete Factories ---")
cc_factory = CreditCardFactory()
result1 = cc_factory.some_operation()
print(f"Credit Card: {result1}")

pp_factory = PayPalFactory()
result2 = pp_factory.some_operation()
print(f"PayPal: {result2}")

crypto_factory = CryptoFactory()
result3 = crypto_factory.some_operation()
print(f"Crypto: {result3}")

# Test using ShapeFactory (static method)
print("\n--- Using ShapeFactory (Static Method) ---")
processor1 = ShapeFactory.create("creditcard")
print(f"Credit Card: {processor1.operation()}")

processor2 = ShapeFactory.create("paypal")
print(f"PayPal: {processor2.operation()}")

processor3 = ShapeFactory.create("crypto")
print(f"Crypto: {processor3.operation()}")

# Test error handling
print("\n--- Error Handling ---")
try:
    processor4 = ShapeFactory.create("invalid")
    print(processor4.operation())
except ValueError as e:
    print(f"Error: {e}")