from abc import ABC, abstractmethod

from template_method.gateway import Gateway


class NewPaymentProcessor(ABC):
    def __init__(self, amount: float, gateway: Gateway):
        self._amount = amount
        self._gateway = gateway

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount

    @property
    def gateway(self) -> Gateway:
        return self._gateway

    @gateway.setter
    def gateway(self, gateway: Gateway):
        self._gateway = gateway

    @abstractmethod
    def calculate_discount(self) -> float:
        pass

    def calculate_fee(self) -> float:
        return 0

    def process_charge(self) -> bool:
        final_value = self.amount + self.calculate_fee() - self.calculate_discount()
        print(f"{self.amount} + {self.calculate_fee()} - {self.calculate_discount()} = {final_value}")
        return self.gateway.charge(final_value)
