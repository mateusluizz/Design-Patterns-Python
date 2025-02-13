from observer.observer import Observer


class Email:
    @staticmethod
    def enviar_email(observer: Observer, message: str) -> None:
        print("-" * 60)
        print(f"Email sent to {observer.get_nome()} - {observer.get_email()}")
        print(f"Message: {message}")
