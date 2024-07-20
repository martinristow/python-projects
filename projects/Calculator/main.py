# Calculator
from art import logo

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtrack(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# + - * / -> Keys
# names of functions -> Values
operations = {
    "+": add,
    "-": subtrack,
    "*": multiply,
    "/": divide
}


def calculation():
    print(logo)
    num1 = float(input("What's the first number?"))

    for operation in operations:
        print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} =  {answer}")

        ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
        if ask == "y":
            num1 = answer
        else:
            should_continue = False
            calculation()

calculation()

