num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")