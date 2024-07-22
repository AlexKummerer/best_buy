from typing import List
from products import Product


class Store:
    """
    A class to represent a store
    """

    def __init__(self, products: List[Product]) -> None:
        """
        Initialize a store

        Args:
            products (List[Product]): the products in the store
        """
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product) -> None:
        """
        Add a product to the store

        Args:
            product (Product):  the product to add
        """
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store

        Args:
            product (Product): the product to remove
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all products in the store

        Returns:
            int:  the total quantity of all products in the store
        """
        return sum([product.get_quantity() for product in self.products])

    def get_all_products(self) -> List[Product]:
        """
        Get all products in the store

        Returns:
            List[Product]:  all products in the store
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Make an order

        Args:
            shopping_list (List[tuple]):  a list of tuples,
            each containing a product and the quantity to order

        Raises:
            ValueError:  if the product is not found or there is not enough stock

        Returns:
            float:  the total price of the order
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products and product.get_quantity() >= quantity:
                total_price += product.buy(quantity)
            else:
                raise ValueError("Product not found or not enough stock")

        return total_price
