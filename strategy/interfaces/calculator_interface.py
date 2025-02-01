from abc import ABC, abstractmethod


class CalculatorStrategy(ABC):
    @abstractmethod
    def calculate(self, num1: float, num2: float) -> float:
        pass
