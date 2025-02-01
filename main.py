from strategy.context.calculator import Calculator
from strategy.strategies.div import Div
from strategy.strategies.multi import Multi
from strategy.strategies.sub import Sub
from strategy.strategies.sum import Sum


def main():
    sum_strategy = Sum()
    sub_strategy = Sub()
    div_strategy = Div()
    multi_strategy = Multi()

    number_1 = 20
    number_2 = 4

    # Individual objects

    sum_result = Calculator(sum_strategy).calculate(number_1, number_2)
    sub_result = Calculator(sub_strategy).calculate(number_1, number_2)
    div_result = Calculator(div_strategy).calculate(number_1, number_2)
    multi_result = Calculator(multi_strategy).calculate(number_1, number_2)

    # Changing the strategy at runtime

    calc = Calculator(sum_strategy)
    print(calc.calculate(number_1, number_2))
    calc.set_strategy(sub_strategy)
    print(calc.calculate(number_1, number_2))
    calc.set_strategy(div_strategy)
    print(calc.calculate(number_1, number_2))
    calc.set_strategy(multi_strategy)
    print(calc.calculate(number_1, number_2))

    print(sum_result, sub_result, div_result, multi_result)


if __name__ == "__main__":
    main()
