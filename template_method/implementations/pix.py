from template_method.abstract.payment import PaymentProcessor


class PixPayment(PaymentProcessor):
    def validate_payment(self):
        print("Validating PIX key...")

    def make_payment(self):
        print(f"Payment of R${self.amount:.2f} made with PIX.")
