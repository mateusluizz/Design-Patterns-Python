from strategy.interfaces.shipping_interface import ShippingStrategy


class Shipping:
    def __init__(self, strategy: ShippingStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> ShippingStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ShippingStrategy):
        self._strategy = strategy

    def calculate(self, order_value: float) -> float:
        return self._strategy.calculate_shipping(order_value)
