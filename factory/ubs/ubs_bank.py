from factory.bank import Bank
from factory.bank_slip import BankSlip
from factory.ubs.ubs_10_days import Ubs10Days
from factory.ubs.ubs_30_days import Ubs30Days
from factory.ubs.ubs_60_days import Ubs60Days


class UbsBank(Bank):
    def _create_bank_slip(self, slip_due_date, amount) -> BankSlip:
        match slip_due_date:
            case 10:
                return Ubs10Days(amount)
            case 30:
                return Ubs30Days(amount)
            case 60:
                return Ubs60Days(amount)
            case _:
                raise Exception("Due date not supported")
