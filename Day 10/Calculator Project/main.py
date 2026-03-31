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
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    should_accumulate = True

    num1 = float(input("Enter first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation = input("Enter operation from above options: ")
        num2 = float(input("Enter second number: "))

        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        ask = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if ask == "y":
            num1 = result
        elif ask == "n":
            should_accumulate = False
            print("\n" * 100)
            calculator()

calculator()