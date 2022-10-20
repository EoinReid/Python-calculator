# user interface
number_one = input("Enter a number: ")
number_two = input("Enter another number: ")

#calculations
operation = input("Choose an operation: + - * /")
# if user enters +, do addition
# making sure to convert number_one and number_two to int, as the variables are a str due to taking user input.
# e.g without converting to int if user enters 5 and 10 for number_one and number_two and chooses + the result will be 510, instead of 15.
if operation == "+":
    print(int(number_one) + int(number_two))
# else if user enters -, do subtraction
# using max() and min() to prevent a negative number and ensuring the bigger number is always subtracted by the smallerst.
elif operation == "-":
    print(max(int(number_one), int(number_two)) - min(int(number_one), int(number_two)))
# else if user enters *, do multiplication
# converting to integer similar to addition operation
elif operation == "*":
    print(int(number_one)*int(number_two))
# else if user enters /, do division
elif operation == "/":
    print(max(number_one, number_two)/min(number_one, number_two))
# else if the user enters anything other than the above 4 operators, display a warning that they are not entering a valid operator.
else:
    print("Not a valid operator, please try again.")