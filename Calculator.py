print("**************")
print("**Calculator**")
print("**************")

def validate_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def validate_operation(prompt):
    while True:
        op = input(prompt).strip()
        if op in {"+", "-", "*", "/"}:
            return op
        else:
            print("Invalid operation. Please use +, -, *, or /.")

# User Input
operation = validate_operation("Enter the operation (+, -, *, /): ")
num1 = validate_number("Enter first number: ")
num2 = validate_number("Enter second number: ")

# Calculation Logic
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2

# Output
print(f"\nResult: {num1} {operation} {num2} = {round(result, 4)}")