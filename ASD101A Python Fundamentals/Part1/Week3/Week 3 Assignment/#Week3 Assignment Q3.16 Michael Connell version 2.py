#Week3 Assignment Q3.16 Michael Connell Version 2

# Comparison operators:
# != : Not equal to
# == : Equal to
# < : Less than
# > : Greater than

a = 2
b = 4
c = 6

val1 = input("Enter a value for comparison: ")
comparison = input("Enter a comparison operator (!=, ==, <, >): ")
val2 = input("Enter a second value for comparison: ")

if comparison == "!=":
    if val1 != val2:
        print("True")
    else:
        print("False")
elif comparison == "==":
    if val1 == val2:
        print("True")
    else:
        print("False")
elif comparison == "<":
    if val1 < val2:
        print("True")
    else:
        print("False")
elif comparison == ">":
    if val1 > val2:
        print("True")
    else:
        print("False")
else:
    print("Invalid operator")
