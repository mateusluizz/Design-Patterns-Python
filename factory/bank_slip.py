from abc import ABC


class BankSlip(ABC):
    _fee: float
    _discount: float
    _fine: float

    def __init__(self, amount: float):
        self.amount = amount

    def calculate_fee(self) -> float:
        return self.amount * self._fee

    def calculate_discount(self) -> float:
        return self.amount * self._discount

    def calculate_fine(self) -> float:
        return self.amount * self._fine
