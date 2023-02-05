#Take Away Journal Question 4 Michael Connell

# Define the range
lower_bound = 1
upper_bound = 100

while True:
    # Get user input
    value = int(input("Enter a value: "))

    # Check if value is in range
    if value in range(lower_bound, upper_bound + 1):
        print("The value is in the range.")
        break
    else:
        print("The value is not in the range. Try again.")
