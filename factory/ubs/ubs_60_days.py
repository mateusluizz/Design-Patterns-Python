from factory.bank_slip import BankSlip


class Ubs60Days(BankSlip):
    def __init__(self, amount: float):
        super().__init__(amount)
        self._fee = 0.1
        self._discount = 0
        self._fine = 0.15
