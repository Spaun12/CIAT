#Week3 Assignment Q3.15 Michael Connell
# Get input from user
val1 = input("Enter the first value (True or False): ")
val2 = input("Enter the second value (True or False): ")

# Convert input to Boolean
val1 = val1.lower() == "true"
val2 = val2.lower() == "true"

# Get the logical operator from the user
operator = input("Enter the logical operator (and, or, not): ")

# Check the result of the logical expression
if operator == "and":
    result = val1 and val2
    print(result)
elif operator == "or":
    result = val1 or val2
    print(result)
elif operator == "not":
    result = not val1
    print(result)
else:
    print("Invalid operator")