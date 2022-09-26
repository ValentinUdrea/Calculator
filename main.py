# Calculator
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    end = False
    while not end:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        do_y_continue = input(
            f"Type 'y' to continue calculating with {first_answer}, type 'n' to exit or type 'c' to start over.")
        if do_y_continue == "y":
            operation_symbol = input("Pick an operation: ")
            num3 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(first_answer, num3)
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        elif do_y_continue == 'c':
            # We are using Recursion here
            calculator()  # -- > this will take us all the way back to the beginning
        else:
            end = True
            print("Thank you for using my calculator! ")


calculator()