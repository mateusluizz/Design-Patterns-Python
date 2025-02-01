from strategy.interfaces.calculator_interface import CalculatorStrategy


class Sum(CalculatorStrategy):
    def calculate(self, num1: float, num2: float) -> float:
        return num1 + num2
