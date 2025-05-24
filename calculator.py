# Simple Calculator
print("Welcome to the Simple Calculator!")
print("-" * 50)

try:
    # Input for numbers and operation
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ").strip()

    # Perform the operation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:  # Check for division by zero
            result = first_number / second_number
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Error: Invalid operation."

    # Print the result
    print("-" * 50)
    print(f"Result: {result}")
    print("-" * 50)

except ValueError:
    print("-" * 50)
    print("Error: Please enter valid numbers.")
    print("-" * 50)
