"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
# """
# def run_calculator(string):
#     """ doc string needed"""
#     while True:
#         tokens = string.split(" ")
#         operator = tokens[0]
#         if operator == 'q':
#             break
#         elif operator == "+":
#             return add(int(tokens[1]), int(tokens[2]))
#         elif operator == "-":
#             return subtract(int(tokens[1]), int(tokens[2]))
#         elif operator == "*":
#             return multiply(int(tokens[1]), int(tokens[2]))
#         elif operator == "/":
#             return divide(int(tokens[1]), int(tokens[2]))
#         elif operator == "square":
#             return square(int(tokens[1]))
#         elif operator == "cube":
#             return cube(int(tokens[1]))
#         elif operator == "pow":
#             return power(int(tokens[1]), int(tokens[2]))
#         elif operator == "mod":
#             return mod(int(tokens[1]), int(tokens[2]))
#         else:
#             print "ERROR: The operator is not defined"
# """

operators = {"+": add, "-": subtract, "*": multiply, "%": mod,
             "/": divide, "**": power, "square": square, "cube": cube}


def run_calculator(string, operators):
    while True:
        tokens = string.split(" ")
        operator = tokens[0]
        if operator == 'q':
            break
        elif operator not in operators:
            print "ERROR: The operator is not defined"
        else:
            a = generate_operator(tokens, operator, operators)
            if len(tokens) ==2:
                return a[0](a[1])
            else:
                return a[0](a[1], a[2])

def generate_operator(tokens, operator, operators):
    if len(tokens) == 2:
        return [operators[operator], int(tokens[1])]
    else:
        return [operators[operator], int(tokens[1]), int(tokens[2])]

input_string = "cube 3"
print run_calculator(input_string, operators)