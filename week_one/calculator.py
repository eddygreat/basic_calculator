# DizEmpires Basic Calculator
# This program allows the user to perform basic arithmetic operations (+, -, *, /) on two numbers.

def main():
    # Display a welcome message
    print("Welcome to DizEmpires Basic Calculator")
    print("Let's solve some math problems!")

    # Prompt the user to enter the first number
    num1 = float(input("Enter your first number: "))

    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Ask the user to choose an operation
    op = input("Please choose an operation (+, -, *, /): ")

    # Perform the selected operation and display the result
    if op == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif op == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif op == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif op == '/':
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero.")
    else:
        # Handle invalid operation input
        print("Invalid operation. Please enter one of +, -, *, or /.")

# Run the calculator program if this file is executed directly
if __name__ == "__main__":
    main()
