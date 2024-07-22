from abc import ABC, abstractmethod


class Promotion(ABC):
    """
     promotion class

    Args:
        ABC (_type_):  abstract class
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, total: float) -> float:
        """
        Apply the promotion

        Args:
            total (float):  the total price

        Returns:
            float:  the total price after the promotion
        """
        pass


class PercentDiscount(Promotion):
    """
    A class to represent a percent discount promotion

    Args:
        Promotion (_type_):  the base promotion class
    """

    def __init__(self, name: str, percent: float):
        """
        Initialize a percent discount promotion

        Args:
            name (str):  the name of the promotion
            percent (float):  the percent discount
        """
        super().__init__(name)
        self.percent = percent

    def apply(self, total: float) -> float:
        """
        Apply the percent discount promotion

        Args:
            total (float):  the total price

        Returns:
            float:  the total price after the promotion
        """
        return total * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """
    A class to represent a second half price promotion

    Args:
        Promotion (_type_):  the base promotion class
    """

    def __init__(self, name: str):
        """
        Initialize a second half price promotion

        Args:
            name (str):  the name of the promotion
        """
        super().__init__(name)

    def apply(self, total: float) -> float:
        """
        Apply the second half price promotion

        Args:
            total (float):  the total price

        Returns:
            float:  the total price after the promotion
        """
        return total * 0.5


class ThirdOneFree(Promotion):
    """
    A class to represent a third one free promotion

    Args:
        Promotion (_type_):  the base promotion class
    """

    def __init__(self, name: str):
        """
        Initialize a third one free promotion

        Args:
            name (str):  the name of the promotion
        """
        super().__init__(name)

    def apply(self, total: float) -> float:
        """
        Apply the third one free promotion

        Args:
            total (float):  the total price

        Returns:
            float:  the total price after the promotion
        """
        num_items = total // 1  # Number of whole items
        num_free_items = num_items // 3
        discount = (total / num_items) * num_free_items if num_items > 0 else 0
        return total - discount
