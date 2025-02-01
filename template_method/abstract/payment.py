from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def __init__(self, amount: float):
        self._amount = amount

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount

    def process_payment(self):
        self.validate_payment()
        self.make_payment()
        self.send_receipt()
        print("Payment finalized.\n")

    @abstractmethod
    def validate_payment(self):
        pass

    @abstractmethod
    def make_payment(self):
        pass

    def send_receipt(self):
        print("Receipt sent to the customer.")
