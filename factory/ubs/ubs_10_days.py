from factory.bank_slip import BankSlip


class Ubs10Days(BankSlip):
    def __init__(self, amount: float):
        super().__init__(amount)
        self._fee = 0.03
        self._discount = 0.05
        self._fine = 0.02
