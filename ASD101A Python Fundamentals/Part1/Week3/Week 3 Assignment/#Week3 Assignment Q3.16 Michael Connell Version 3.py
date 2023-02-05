#Week3 Assignment Q3.16 Michael Connell Version3

import ast

a = 2
b = 4
c = 6

#prompt the user to enter a boolean comparison
comp = input("Enter a boolean comparison: ")

try:
    #evaluate the input string as a python literal, passing in the values of a, b and c
    result = ast.literal_eval(comp, {"a": a, "b": b, "c": c})
    # check if the result is true or false
    if result:
        print("True")
    else:
        print("False")
#check for invalid input
except (SyntaxError, ValueError):
    print("Invalid input")

