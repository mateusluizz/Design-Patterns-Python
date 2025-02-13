from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

    @abstractmethod
    def get_nome(self) -> str:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass
