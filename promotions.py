from abc import ABC, abstractmethod


class Promotion(ABC):
    """Base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, total: float, price_per_item: float, quantity: int) -> float:
        """Apply the promotion."""
        pass


class PercentDiscount(Promotion):
    """Percent discount promotion."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100")
        self.percent = percent

    def apply(self, total: float, price_per_item: float, quantity: int) -> float:
        return total * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Second half-price promotion."""

    def apply(self, total: float, price_per_item: float, quantity: int) -> float:
        if quantity >= 2:
            half_price_items = quantity // 2
            full_price_items = quantity - half_price_items
            return (full_price_items * price_per_item) + (
                half_price_items * price_per_item * 0.5
            )
        return total


class ThirdOneFree(Promotion):
    """Third-one-free promotion."""

    def apply(self, total: float, price_per_item: float, quantity: int) -> float:
        free_items = quantity // 3
        return total - (free_items * price_per_item)
