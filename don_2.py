import math


def calculator():


    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error! Can't divide by zero!."
        return a / b

    def square(a,b):
        return a ** b

    def root(a,b):
        if a<0:
            return ("Error! Can't be less than or equal to zero.")
        return math.sqrt(a)

    def choose_operation(operation):
        def get_numbers():
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2

        num1, num2 = get_numbers()

        if operation == '1':
            return add(num1, num2)
        elif operation == '2':
            return subtract(num1, num2)
        elif operation == '3':
            return multiply(num1, num2)
        elif operation == '4':
            return divide(num1, num2)
        elif operation == '5':
            return square(num1, num2)
        elif operation == '6':
            return root(num1, num2)
        else:
            return "Invalid operation."


    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Root Number")
    print("7. Exit")

    while True:
        choice = input("Enter the number of the operation you want to perform (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            result = choose_operation(choice)
            print(f"The result is: {result}")
        else:
            print("Invalid input. Please try again.")

calculator()


