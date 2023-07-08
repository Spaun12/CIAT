#Student: Michael D. Connell Jr.
#Date: 2023-07-01
#Recursion

# Let's use the built-in 'input' function is used to take an integer input from the user.
# This is the number for which we'll calculate the factorial.
# The 'int' function is used to convert the input, which is a string by default, to an integer.

def factorial(n):
    """
    Here is the recursive function to calculate the factorial of a number.
    Arguments:
    n -- the number for which to calculate the factorial
    Returns:
    The factorial of 'n'
    """

    # A factorial is undefined for negative numbers.
    # If 'n' is negative, we will raise an exception.
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")

    # The factorial of 0 is 1.
    # This is our base case for the recursion.
    # Without a base case, the recursion would go on indefinitely.
    elif n == 0:
        return 1

    # If 'n' is neither negative nor 0, we recursively calculate the factorial.
    else:
        # The factorial of 'n' is 'n' times the factorial of 'n-1'.
        # This is where the recursion happens:
        # 'factorial(n)' is defined in terms of 'factorial(n-1)', which is defined in terms of 'factorial(n-2)', and so on,
        # until we reach 'factorial(0)', which we've defined to be 1 (our base case).
        return n * factorial(n - 1)

while True:  # This loop will keep running until we explicitly break out of it.
    user_input = int(input("Please enter a non-negative integer: "))
    
    try:
        print("The factorial of " + str(user_input) + " is " + str(factorial(user_input)))
    except ValueError as e:
        print(e)
        
    # After calculating and printing the factorial, ask the user if they want to continue.
    continue_answer = input("Do you want to calculate another factorial? (yes/no): ")

    # If the user's answer isn't 'yes', break out of the loop.
    if continue_answer.lower() != 'yes':
        break
