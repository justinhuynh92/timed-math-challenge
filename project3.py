#randomly generate operands
import random
import time

OPERATORS = ["+", "-", "/", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

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

#set up timer once started
wrong = 0
input("Press enter to start!")
print("-----")

start_time = time.time()

#ask for number of problems then set up a time
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    #keep asking until it gets it correct
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
#round total time to the nearest 2 digits
total_time = round(end_time - start_time, 2)

print("-----")
print("Nice work! You finished in", total_time, "seconds!")
