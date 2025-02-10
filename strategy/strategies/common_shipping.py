from strategy.interfaces.shipping_interface import ShippingStrategy


class CommonShipping(ShippingStrategy):
    def calculate_shipping(self, order_value: float) -> float:
        return order_value * 0.05
