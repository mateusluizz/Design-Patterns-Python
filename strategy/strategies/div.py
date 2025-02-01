from decimal import DivisionByZero

from strategy.interfaces.calculator_interface import CalculatorStrategy


class Div(CalculatorStrategy):
    def calculate(self, num1: float, num2: float) -> float:
        if num2 == 0:
            raise DivisionByZero("Division by zero is not allowed")
        return num1 / num2
