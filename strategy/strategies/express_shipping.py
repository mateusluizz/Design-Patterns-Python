from strategy.interfaces.shipping_interface import ShippingStrategy


class ExpressShipping(ShippingStrategy):
    def calculate_shipping(self, order_value: float) -> float:
        return order_value * 0.1
