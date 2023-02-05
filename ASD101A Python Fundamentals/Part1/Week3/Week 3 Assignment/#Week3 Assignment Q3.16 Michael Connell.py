#Week3 Assignment Q3.16 Michael Connell

# Comparison operators:
# != : Not equal to
# == : Equal to
# < : Less than
# > : Greater than

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

val1 = int(input("Enter a value for comparison: "))
comparison = input("Enter a comparison operator (!=, ==, <, >): ")
val2 = int(input("Enter a second value for comparison: "))

if comparison == "!=":
    if (val1 == a and val2 != b) or (val1 == b and val2 != a) or (val1 == c and val2 != a) or (val1 == a and val2 != c) or (val1 == b and val2 != c) or (val1 == c and val2 != b):
        print("True")
    else:
        print("False")
elif comparison == "==":
    if (val1 == a and val2 == b) or (val1 == b and val2 == a) or (val1 == c and val2 == a) or (val1 == a and val2 == c) or (val1 == b and val2 == c) or (val1 == c and val2 == b):
        print("True")
    else:
        print("False")
elif comparison == "<":
    if (val1 == a and val2 > b) or (val1 == b and val2 > a) or (val1 == c and val2 > a) or (val1 == a and val2 > c) or (val1 == b and val2 > c) or (val1 == c and val2 > b):
        print("True")
    else:
        print("False")
elif comparison == ">":
    if (val1 == a and val2 < b) or (val1 == b and val2 < a) or (val1 == c and val2 < a) or (val1 == a and val2 < c) or (val1 == b and val2 < c) or (val1 == c and val2 < b):
        print("True")
    else:
        print("False")
else:
    print("Invalid operator")
