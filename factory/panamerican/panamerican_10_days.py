from factory.bank_slip import BankSlip


class Panamerican10Days(BankSlip):
    def __init__(self, amount: float):
        super().__init__(amount)
        self._fee = 0.02
        self._discount = 0.1
        self._fine = 0.05
