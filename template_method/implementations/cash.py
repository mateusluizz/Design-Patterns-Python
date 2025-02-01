from template_method.abstract.new_payment import NewPaymentProcessor


class CashPayment(NewPaymentProcessor):
    def calculate_discount(self) -> float:
        return self.amount * 0.1
