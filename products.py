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
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

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
        Return the string representation of the product

        Returns:
            str: _description_
        """
        return f"{self.name}, Price: {self.price}, Quntity {self.quantity}"

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
