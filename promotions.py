from abc import ABC, abstractmethod


class Promotion(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class PercentDiscount(Promotion):

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply(self, total: float) -> float:
        return total * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):

    def __init__(self, name: str):
        super().__init__(name)

    def apply(self, total: float) -> float:
        return total * 0.5


class ThirdOneFree(Promotion):

    def __init__(self, name: str):
        super().__init__(name)

    def apply(self, total: float) -> float:
        return total * 0.67
