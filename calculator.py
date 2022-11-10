# Calculator
from calculator_art import logo


# Add
def add(num1, num2):
    return num1 + num2


# Subtract
def sub(num1, num2):
    return num1 - num2


# Multiply
def mul(num1, num2):
    return num1 * num2


# Divide
def div(num1, num2):
    return num1 / num2


calculate = {   #Dictionary to hold all the operations
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    print(logo)

    num1 = float(input("Enter first number: "))
    for symbol in calculate:   #Will print all the operations without printing it line by line
        print(symbol)
    should_continue = True
    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        calculator_function = calculate[operation]   #holds the operation
        result = calculator_function(num1, num2)       #holds the inputs

        print(f"{num1} {operation} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            num1 = result   #num1 will be the result of the previous calculation
        else:
            should_continue = False
            calculator() #recursion to call the functiona again (wiping the data to start a new calculation)


calculator()