from src.patterns.structural.adapter import Adaptee, Adapter, PayPalAPI, PayPalAdapter

print("Testing Adapter Pattern - E-Commerce Payment Integration")
print("=" * 60)

# Test 1: Basic Adapter pattern
print("\n--- Test 1: Basic Adapter ---")
adaptee = Adaptee("PaymentSystem")
adapter = Adapter(adaptee)

result1 = adapter.request(100, "USD")
print(result1)

result2 = adapter.request(250, "EUR")
print(result2)

# Test 2: E-Commerce PayPal Adapter
print("\n--- Test 2: PayPal Payment Adapter ---")
paypal_api = PayPalAPI()
paypal_adapter = PayPalAdapter(paypal_api, "customer@shop.com")

result3 = paypal_adapter.request(150, "USD")
print(result3)

result4 = paypal_adapter.request(100, "EUR")
print(result4)

print("\n" + "=" * 60)
print("✅ Adapter Pattern tests completed!")