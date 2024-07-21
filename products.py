class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def __str__(self) -> str:
        return f"{self.name}, Price: {self.price}, Quntity {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.quantity < quantity:
            raise ValueError("Not enough stock")

        self.set_quantity((self.quantity - quantity))
        return self.price * quantity
