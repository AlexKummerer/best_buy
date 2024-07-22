class Product:
    """
    A class to represent a product
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Initialize a product

        Args:
            name (str): the name of the product
            price (float): the price of the product
            quantity (int):  the quantity of the product

        Raises:
            ValueError:  if the name is empty, the price is negative, or the quantity is negative
        """
        if not name or price <= 0 or quantity < 0:
            raise ValueError("Invalid product parameters")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None

    def get_quantity(self) -> float:
        """
        Get the quantity of the product
        Returns:
            float: the quantity of the product
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Set the quantity of the product

        Args:
            quantity (int):  the quantity of the product

        Raises:
            ValueError:  if the quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """
        Check if the product is active

        Returns:
            bool:  True if the product is active, False otherwise
        """
        return self.active

    def activate(self) -> None:
        """
        Activate the product
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Deactivate the product
        """
        self.active = False

    def __str__(self) -> str:
        """
        Return a string representation of the product

        Returns:
            str: the string representation of the product
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"
        )

    def buy(self, quantity: int) -> float:
        """
        Buy a quantity of the product
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.quantity < quantity:
            raise ValueError("Not enough stock")

        self.set_quantity((self.quantity - quantity))
        return self.price * quantity

    def set_promotion(self, promotion):
        """
        Set the promotion for the product

        Args:
            promotion (_type_):  the promotion to set
        """
        self.promotion = promotion


class LimitedProduct(Product):
    """
    A class to represent a limited product

    Args:
        Product (_type_):  the base product class
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int) -> None:
        super().__init__(name, price, quantity)
        self.maximum = maximum
        """
        Initialize a limited product

        Raises:
            ValueError: if the maximum quantity is negative or less than the current quantity
        """


class NonStockedProduct(Product):
    """
    A class to represent a non-stocked

    Args:
        Product (_type_): the base product class
    """

    def __init__(
        self,
        name: str,
        price: float,
    ) -> None:
        super().__init__(name, price, quantity=0)
        """
        Initialize a non-stocked product
        """

    def set_quantity(self, quantity):
        """
        Set the quantity of the product

        Args:
            quantity (_type_):  the quantity of the product

        Raises:
            ValueError: _description_
        """
        raise ValueError("NonStockedProduct cannot have a quantity.")
