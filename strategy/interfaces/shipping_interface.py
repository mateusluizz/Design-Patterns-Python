from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping(self, order_value: float) -> float:
        pass
