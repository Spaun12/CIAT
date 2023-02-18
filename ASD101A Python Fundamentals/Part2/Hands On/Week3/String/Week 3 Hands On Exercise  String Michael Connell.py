# Week 3: Hands On Exercise - String
#Using While True to make this repeatable
while True:
    # Ask the user to input a series of single-digit numbers with nothing separating them
    digits = input("Enter a series of single-digit numbers with nothing separating them: ")
    # Initialize a variable to hold the sum of the digits
    sum = 0
    # Iterate over each digit in the input string
    for digit in digits:
        # Convert the current digit to an integer and add it to the sum
        sum += int(digit)
    # Print the sum of the digits
    print("The sum of the digits is:", sum)
   
    # Ask the user if they want to try again
    choice = input("Do you want to try again? (Y/N): ")
    # If the user doesn't want to try again, break out of the loop
    if choice.lower() != 'y':
        break