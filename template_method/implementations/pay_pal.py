from template_method.abstract.payment import PaymentProcessor


class PayPalPayment(PaymentProcessor):
    def validate_payment(self):
        print("Validating PayPal account...")

    def make_payment(self):
        print(f"Payment of R${self.amount:.2f} made with PayPal.")
