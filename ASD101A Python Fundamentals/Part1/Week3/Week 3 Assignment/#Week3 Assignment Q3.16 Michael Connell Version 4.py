#Week3 Assignment Q3.16 Michael Connell Version 4

# import the ast module
import ast

# Assign values to variables a, b, and c
a = 2
b = 4
c = 6

# Prompt the user to enter a comparison phrase
comparison = input("Enter a comparison phrase (e.g. 'a >= -1' or 'a <= b'): ")

# Use the ast.parse() function to parse the comparison phrase and store the result in a variable
parsed_comparison = ast.parse(comparison, mode='eval')

# Use eval(compiled_comparison) to evaluate the comparison phrase and print the result
if eval(compile(parsed_comparison, filename='<string>', mode='eval')):
    print("True")
else:
    print("False")
