from products import Product

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

print(bose.__str__())
print(mac.__str__())

bose.set_quantity(1000)
print(bose.__str__())