# Calculator
operation = input("Enter the operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result,4)}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result,4)}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {round(result,4)}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {round(result,4)}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print(f"Error: Invalid operation '{operation}'. Please use +, -, *, or /.")