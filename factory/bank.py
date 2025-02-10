from abc import abstractmethod

from factory.bank_slip import BankSlip


class Bank:
    def generate_bank_slip(self, slip_due_date: int, amount: float) -> BankSlip:
        bank_slip = self._create_bank_slip(slip_due_date, amount)
        print("=" * 40)
        print(f"Slip for {amount} has been generated with the value of {amount}")
        print(f"Fee Value: {bank_slip.calculate_fee()}")
        print(f"Discount Value: {bank_slip.calculate_discount()}")
        print(f"Fine Value: {bank_slip.calculate_fine()}")
        print("=" * 40)
        print()
        return bank_slip

    @abstractmethod
    def _create_bank_slip(self, slip_due_date: int, amount: float) -> BankSlip:
        pass
