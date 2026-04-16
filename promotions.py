from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract Base Class for Promotions
    """

    def __init__(self, promotion_text):
        self.promotion_text = promotion_text

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    """
    Every second item of product has half the price
    """

    def __init__(self, promotion_text):
        super().__init__(promotion_text)

    def apply_promotion(self, product, quantity) -> float:
        reduced_items = quantity // 2
        return (quantity - reduced_items) * product.price + reduced_items * product.price * 0.5


class ThirdOneFree(Promotion):
    """
    Every third item of product is free
    """

    def __init__(self, promotion_text):
        super().__init__(promotion_text)

    def apply_promotion(self, product, quantity) -> float:
        free_items = quantity // 3
        return (quantity - free_items) * product.price


class PercentDiscount(Promotion):
    """
    Every item of product is reduced by given percentage.
    """

    def __init__(self, promotion_text, percent):
        super().__init__(promotion_text)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        return quantity * product.price * (1 - self.percent / 100)
