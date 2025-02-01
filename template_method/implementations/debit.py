from template_method.abstract.new_payment import NewPaymentProcessor


class DebitPayment(NewPaymentProcessor):
    def calculate_fee(self) -> float:
        return 4

    def calculate_discount(self) -> float:
        return self.amount * 0.05
