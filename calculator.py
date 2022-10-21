# user interface
# convert user input (which defaults as string, to float)
number_one = float(input("Enter a number: "))
number_two = float(input("Enter another number: "))
operation = input("Choose an operation: + - * /")

# functions for calculations
def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

#calculations
# if user enters +, do addition
if operation == "+":
    # calls add() method to do calculations instead of doing it within the if statement
    # No longer converting type in if statement but at input.
    print(add(number_one, number_two))
# else if user enters -, do subtraction
elif operation == "-":
    # calls minus() method to do calucation
    print(minus(number_one, number_two))
# else if user enters *, do multiplication
# converting to integer similar to addition operation
elif operation == "*":
    print(multiply(number_one, number_two))
# else if user enters /, do division
elif operation == "/":
    print(divide(number_one, number_two))
# else if the user enters anything other than the above 4 operators, display a warning that they are not entering a valid operator.
else:
    print("Not a valid operator, please try again.")