from typing import List
from products import Product


class Store:
    """A class to represent a store."""

    def __init__(self, products: List[Product]) -> None:
        if not all(isinstance(p, Product) for p in products):
            raise ValueError("All items must be Product instances")
        
        print("Store created")
        print("Products in store:", products)
        self.products = products

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """Make an order and return total cost."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise ValueError("Invalid product in shopping list")
            total_price += product.buy(quantity)
        return total_price
