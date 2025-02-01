from template_method.abstract.payment import PaymentProcessor


class CreditCardPayment(PaymentProcessor):
    def validate_payment(self):
        print("Validating credit card...")

    def make_payment(self):
        print(f"Payment of R${self.amount:.2f} made with credit card.")
