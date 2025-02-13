from typing import List

from observer.observer import Observer
from observer.subject import Subject


class Newsletter(Subject):
    def __init__(self):
        self.observers: List[Observer] = []
        self.messages: List[str] = []

    def register_observer(self, observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer) -> None:
        for obs in self.observers:
            if obs == observer:
                self.observers.remove(obs)

    def notify_observers(self) -> None:
        for obs in self.observers:
            obs.update(self.messages[-1])

    def add_message(self, message: str) -> None:
        self.messages.append(message)
        self.notify_observers()
