from strategy.interfaces.calculator_interface import CalculatorStrategy


class Calculator:
    def __init__(self, strategy: CalculatorStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> CalculatorStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: CalculatorStrategy):
        self._strategy = strategy

    def calculate(self, num1: float, num2: float) -> float:
        return self._strategy.calculate(num1, num2)
