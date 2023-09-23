#randomly generate operands
import random

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

#write function that generates a problem
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    #randomly select element from a list
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    #evaluate a string as if it was a python expression
    answer = eval(expr)
    return expr, answer

expr, answer = generate_problem()
print(expr, answer)
 