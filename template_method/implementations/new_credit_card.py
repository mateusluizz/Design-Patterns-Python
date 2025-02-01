from template_method.abstract.new_payment import NewPaymentProcessor


class CreditCardNewPayment(NewPaymentProcessor):
    def calculate_fee(self) -> float:
        return self.amount * 0.05

    def calculate_discount(self) -> float:
        if self.amount > 300:
            return self.amount * 0.02
        return 0
