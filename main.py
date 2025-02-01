from strategy.context.calculator import Calculator
from strategy.strategies.div import Div
from strategy.strategies.multi import Multi
from strategy.strategies.sub import Sub
from strategy.strategies.sum import Sum
from template_method.gateway import Gateway
from template_method.implementations import cash
from template_method.implementations.credit_card import CreditCardPayment
from template_method.implementations.debit import DebitPayment
from template_method.implementations.new_credit_card import CreditCardNewPayment
from template_method.implementations.pay_pal import PayPalPayment
from template_method.implementations.pix import PixPayment


def strategy():
    sum_strategy = Sum()
    sub_strategy = Sub()
    div_strategy = Div()
    multi_strategy = Multi()

    number_1 = 20
    number_2 = 4

    # Individual objects

    sum_result = Calculator(sum_strategy).calculate(number_1, number_2)
    sub_result = Calculator(sub_strategy).calculate(number_1, number_2)
    div_result = Calculator(div_strategy).calculate(number_1, number_2)
    multi_result = Calculator(multi_strategy).calculate(number_1, number_2)

    # Changing the strategy at runtime

    calc = Calculator(sum_strategy)
    print(calc.calculate(number_1, number_2))
    calc.strategy = sub_strategy
    print(calc.calculate(number_1, number_2))
    calc.strategy = div_strategy
    print(calc.calculate(number_1, number_2))
    calc.strategy = multi_strategy
    print(calc.calculate(number_1, number_2))

    print(sum_result, sub_result, div_result, multi_result)


def template_method():
    pay_pal_payment = PayPalPayment(100)
    pay_pal_payment.process_payment()

    credit_card_payment = CreditCardPayment(200)
    credit_card_payment.process_payment()

    pix_payment = PixPayment(300)
    pix_payment.process_payment()

    gateway = Gateway()
    value = 1000
    
    print("="*40)
    print("New payment process")
    print("="*40)
    print("")

    debit_payment = DebitPayment(value, gateway)
    debit_payment.process_charge()

    new_credit_card_payment = CreditCardNewPayment(value, gateway)
    new_credit_card_payment.process_charge()

    cash_payment = cash.CashPayment(value, gateway)
    cash_payment.process_charge()


if __name__ == "__main__":
    # strategy()
    template_method()
