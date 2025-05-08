# варіант 1
# def simple_calculator():
#     try:
#         num1 = float(input("Enter the first number: "))
#         operation = input("Enter an action (+, -, *, /): ")
#         num2 = float(input("Enter the second number:"))
#
#         if num2 == 0 and operation == "/":
#             print("Wrong operation! Division by zero is not possible!")
#             return
#
#         if operation == "+":
#             result = num1 + num2
#         elif operation == "-":
#             result = num1 - num2
#         elif operation == "*":
#             result = num1 * num2
#         elif operation == "/":
#             result = num1 / num2
#
#         print(f"Result: {result}")
#
#     except ValueError:
#         print("Wrong operation! Division by zero is not possible!")
#
# simple_calculator()

# варіант 2
from pywebio.input import input, FLOAT, select, NUMBER
from pywebio.output import put_text, put_html, put_error
from tornado.options import options

# HEADER
put_html("<h1>Calculator</h1>")

num3 = input("Enter the first number: ", type=FLOAT)
operation = select("Enter an action : ", options=["+", "-", "*", "/"])
num4 = input("Enter the second number:", type=FLOAT)

if num4 == 0 and operation == "/":
    put_text("Wrong operation! Division by zero is not possible!")
else:
    if operation == "+":
        result = num3 + num4
    elif operation == "-":
        result = num3 - num4
    elif operation == "*":
        result = num3 * num4
    elif operation == "/":
        result = num3 / num4

    put_text(f"Result: {result}")

pass
