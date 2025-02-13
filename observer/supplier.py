from observer.email import Email
from observer.observer import Observer
from observer.subject import Subject


class Supplier(Observer):
    def __init__(self, name: str, email: str, subject: Subject):
        self.__name = name
        self.__email = email
        self.__subject = subject
        self.__subject.register_observer(self)

    def update(self, message: str):
        Email.enviar_email(self, message=message )

    def get_nome(self):
        return self.__name

    def get_email(self):
        return self.__email
