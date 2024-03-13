# Calculator
from os import system
from art import logo

def add(n1: float, n2: float) -> float:
    """Return the sum of n1 and n2."""
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    """Returns the subtraction of n1 by n2."""
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    """Returns the multiplication of n1 by n2."""
    return n1 * n2


def divide(n1: float, n2: float) -> float | str:
    """return the division of n1 by n2."""
    if n2 == 0:
        return "Cannot divide by 0."
    return n1 / n2


def calculator() -> None:
    num1 = float(input("What's the first number: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        selected_operation = input("Pick an operation: ")
        num2 = float(input("What's the second number: "))

        calc_function = operations[selected_operation]
        answer = calc_function(num1, num2)

        print(f"{num1} {selected_operation} {num2} = {answer}")

        keep_calculating = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ")
        if keep_calculating == "y":
            num1 = answer
        else:
            system("clear")
            calculator()




operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)
calculator()
