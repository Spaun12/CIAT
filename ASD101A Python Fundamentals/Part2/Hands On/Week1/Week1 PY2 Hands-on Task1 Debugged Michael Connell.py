#Week1 PY2 Hands-on Michael Connell
# Test program for debugging

# Initialize a global variable 'z' with value 0
z = 0

# Define a function 'func' that takes no arguments
def func():
    # Get the first number from the user as a floating-point value and assign it to 'x'
    x = float(input('Enter a number: '))
    # Get the second number from the user as a floating-point value and assign it to 'y'
    y = float(input('Enter a number: '))
    # Return the average of the two numbers *Step one for correcting the code
    return x + y / 2

# Call the function and assign its return value to 'z' *Step two for correcting the code
z = func()
# Print the value of 'z', which is the average of the two numbers entered by the user
print('The average of the two numbers you have entered is: ', z)
