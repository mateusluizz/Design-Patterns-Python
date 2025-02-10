from factory.bank import Bank
from factory.bank_slip import BankSlip
from factory.panamerican.panamerican_10_days import Panamerican10Days
from factory.panamerican.panamerican_30_days import Panamerican30Days
from factory.panamerican.panamerican_60_days import Panamerican60Days


class PanamericanBank(Bank):
    def _create_bank_slip(self, slip_due_date, amount) -> BankSlip:
        match slip_due_date:
            case 10:
                return Panamerican10Days(amount)
            case 30:
                return Panamerican30Days(amount)
            case 60:
                return Panamerican60Days(amount)
            case _:
                raise Exception("Due date not supported")
