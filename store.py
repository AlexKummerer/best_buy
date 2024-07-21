from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]) -> None:
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum([product.get_quantity() for product in self.products])

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products and product.get_quantity() >= quantity:
                total_price += product.buy(quantity)
            else:
                raise ValueError("Product not found or not enough stock")

        return total_price
