import store
import products

bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

store = store.Store([bose, mac])
price = store.order([(bose, 5), (mac, 30), (bose, 20)])
print(f"Order cost: {price} dollars.")
