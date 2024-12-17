class Product:
    """
    Represents a general product with optional promotions.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Initialize a product.

        Args:
            name (str): The product name.
            price (float): The product price.
            quantity (int): The available stock.

        Raises:
            ValueError: If name is empty, price is <= 0, or quantity < 0.
        """
        if not name or price <= 0 or quantity < 0:
            raise ValueError("Invalid product parameters")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = None

    def get_quantity(self) -> int:
        """Return the product's available quantity."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Update the product's quantity.

        Args:
            quantity (int): The new quantity.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        self.active = self.quantity > 0

    def is_active(self) -> bool:
        """Check if the product is active."""
        return self.active

    def activate(self) -> None:
        """Mark the product as active."""
        self.active = True

    def deactivate(self) -> None:
        """Mark the product as inactive."""
        self.active = False

    def __repr__(self) -> str:
        """Return a string representation of the product."""
        promotion_info = (
            f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        )
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity: int) -> float:
        """
        Purchase a specified quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price for the purchase.

        Raises:
            ValueError: If quantity is <= 0 or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.quantity < quantity:
            raise ValueError("Not enough stock")
        self.set_quantity(self.quantity - quantity)
        return self.get_price(quantity)

    def set_promotion(self, promotion) -> None:
        """Assign a promotion to the product."""
        self.promotion = promotion

    def get_price(self, quantity: int) -> float:
        """
        Calculate the total price for a specified quantity, applying any promotions.

        Args:
            quantity (int): The quantity to calculate the price for.

        Returns:
            float: The total price.
        """
        total = self.price * quantity
        if self.promotion:
            return self.promotion.apply(total, self.price, quantity)
        return total


class LimitedProduct(Product):
    """
    Represents a product with a purchase limit per order.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int) -> None:
        """
        Initialize a limited product.

        Args:
            name (str): The product name.
            price (float): The product price.
            quantity (int): The available stock.
            maximum (int): The maximum units allowed per order.

        Raises:
            ValueError: If maximum is <= 0.
        """
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum must be positive")
        self.maximum = maximum

    def __repr__(self) -> str:
        """Return a string representation of the limited product."""
        promotion_info = (
            f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        )
        return f"{self.name}, Price: {self.price}, Limited to {self.maximum} per order! {promotion_info}"


class NonStockedProduct(Product):
    """
    Represents a product with unlimited availability.
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Initialize a non-stocked product.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        super().__init__(name, price, quantity=0)
        self.active = True

    def set_quantity(self, quantity: int) -> None:
        """
        Prevent setting a quantity for non-stocked products.

        Raises:
            ValueError: Always raises since quantity cannot be set.
        """
        raise ValueError("NonStockedProduct cannot have a quantity.")

    def buy(self, quantity: int) -> float:
        """
        Purchase a specified quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price for the purchase.

        Raises:
            ValueError: If quantity is <= 0.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        return self.get_price(quantity)

    def __repr__(self) -> str:
        """Return a string representation of the non-stocked product."""
        promotion_info = (
            f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        )
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited{promotion_info}"
