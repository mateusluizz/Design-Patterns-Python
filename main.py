from factory.panamerican.panamerican_bank import PanamericanBank
from factory.ubs.ubs_bank import UbsBank
from observer import newletter
from observer.client import Client
from observer.employee import Employee
from observer.newletter import Newsletter
from observer.supplier import Supplier
from strategy.context.calculator import Calculator
from strategy.context.shipping import Shipping
from strategy.strategies.common_shipping import CommonShipping
from strategy.strategies.div import Div
from strategy.strategies.express_shipping import ExpressShipping
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

    print(
        f"Sum: {sum_result}",
        f"Sub: {sub_result}",
        f"Div: {div_result}",
        f"Multi: {multi_result}",
    )

    print()
    print("=" * 40)
    print("Shipping strategies")
    print("=" * 40)
    print("")

    # Shipping

    common_shipping = CommonShipping()
    express_shipping = ExpressShipping()

    shipping = Shipping(common_shipping)

    print(f"Common Shipping: {shipping.calculate(100)}")
    shipping.strategy = express_shipping
    print(f"Express Shipping: {shipping.calculate(100)}")


def template_method():
    pay_pal_payment = PayPalPayment(100)
    pay_pal_payment.process_payment()

    credit_card_payment = CreditCardPayment(200)
    credit_card_payment.process_payment()

    pix_payment = PixPayment(300)
    pix_payment.process_payment()

    gateway = Gateway()
    value = 1000

    print("=" * 40)
    print("New payment process")
    print("=" * 40)
    print("")

    debit_payment = DebitPayment(value, gateway)
    debit_payment.process_charge()

    new_credit_card_payment = CreditCardNewPayment(value, gateway)
    new_credit_card_payment.process_charge()

    cash_payment = cash.CashPayment(value, gateway)
    cash_payment.process_charge()


def factory():
    print("Panamerican")

    panam_bank = PanamericanBank()
    panam_bank.generate_bank_slip(10, 100)
    panam_bank.generate_bank_slip(30, 100)
    panam_bank.generate_bank_slip(60, 100)

    print("UBS")

    ubs_bank = UbsBank()
    ubs_bank.generate_bank_slip(10, 100)
    ubs_bank.generate_bank_slip(30, 100)
    ubs_bank.generate_bank_slip(60, 100)


def observer():
    newsletter = Newsletter()

    employee_1 = Employee("Employee1", "employee1@email.com", newsletter)
    employee_2 = Employee("Employee2", "employee2@email.com", newsletter)

    client_1 = Client("Client1", "client1@email.com", newsletter)
    client_2 = Client("Client2", "client2@email.com", newsletter)

    supplier_1 = Supplier("Supplier1", "supplier1@email.com", newsletter)
    supplier_2 = Supplier("Supplier2", "supplier2@email.com", newsletter)

    newsletter.add_message("First Message")

    print()
    print("#" * 20)

    newsletter.remove_observer(client_2)
    newsletter.remove_observer(employee_1)
    newsletter.remove_observer(supplier_2)

    newsletter.add_message("Second Message")

    print()
    print("#" * 20)

    newsletter.remove_observer(employee_2)
    newsletter.remove_observer(supplier_1)

    newsletter.add_message("Third Message")


if __name__ == "__main__":
    # strategy()
    # template_method()
    # factory()
    observer()
