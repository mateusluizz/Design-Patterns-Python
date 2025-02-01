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

    def calculate(self, a, b) -> float:
        return self._strategy.calculate(a, b)
